"""Энкодеры для сжатия признаков до размерности n_qubits."""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import torch

class PCAEncoder:
    """PCA энкодер для сжатия до latent_dim."""
    
    def __init__(self, latent_dim: int = 8, standardize: bool = True):
        self.latent_dim = latent_dim
        self.standardize = standardize
        self.scaler = StandardScaler() if standardize else None
        self.pca = PCA(n_components=latent_dim)
        self.is_fitted = False
    
    def fit(self, X):
        """X: (n_samples, n_features) — обучающие данные."""
        if self.standardize:
            X_scaled = self.scaler.fit_transform(X)
        else:
            X_scaled = X
        self.pca.fit(X_scaled)
        self.is_fitted = True
        return self
    
    def transform(self, X):
        if not self.is_fitted:
            raise RuntimeError("Encoder не обучен. Вызовите .fit() сначала.")
        if self.standardize:
            X_scaled = self.scaler.transform(X)
        else:
            X_scaled = X
        Z = self.pca.transform(X_scaled)
        # Нормализуем в диапазон [-π, π] для входов RY
        Z = np.clip(Z / (2 * np.std(Z, axis=0) + 1e-8), -np.pi, np.pi)
        return Z.astype(np.float32)

class AutoencoderEncoder:
    """Автоэнкодер на PyTorch (если нужно больше гибкости)."""
    
    def __init__(self, input_dim: int, latent_dim: int = 8, lr: float = 1e-3, epochs=100):
        self.latent_dim = latent_dim
        self.input_dim = input_dim
        self.lr = lr
        self.epochs = epochs
        self.model = None
        self.scaler = StandardScaler()
        self.is_fitted = False
    
    def fit(self, X):
        import torch
        import torch.nn as nn
        import torch.optim as optim
        
        self.scaler.fit(X)
        X_scaled = self.scaler.transform(X).astype(np.float32)
        
        class AE(nn.Module):
            def __init__(self, d_in, d_latent):
                super().__init__()
                self.encoder = nn.Sequential(
                    nn.Linear(d_in, 64),
                    nn.ReLU(),
                    nn.Linear(64, 32),
                    nn.ReLU(),
                    nn.Linear(32, d_latent),
                )
                self.decoder = nn.Sequential(
                    nn.Linear(d_latent, 32),
                    nn.ReLU(),
                    nn.Linear(32, 64),
                    nn.ReLU(),
                    nn.Linear(64, d_in),
                )
            def forward(self, x):
                z = self.encoder(x)
                return self.decoder(z), z
        
        model = AE(self.input_dim, self.latent_dim)
        optimizer = optim.Adam(model.parameters(), lr=self.lr)
        criterion = nn.MSELoss()
        
        dataset = torch.utils.data.TensorDataset(torch.tensor(X_scaled))
        loader = torch.utils.data.DataLoader(dataset, batch_size=128, shuffle=True)
        
        for epoch in range(self.epochs):
            for batch in loader:
                x = batch[0]
                recon, _ = model(x)
                loss = criterion(recon, x)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
        self.model = model
        self.is_fitted = True
        return self
    
    def transform(self, X):
        if not self.is_fitted:
            raise RuntimeError("Autoencoder не обучен.")
        import torch
        X_scaled = self.scaler.transform(X).astype(np.float32)
        with torch.no_grad():
            _, Z = self.model(torch.tensor(X_scaled))
        Z = Z.numpy()
        Z = np.clip(Z / (2 * np.std(Z, axis=0) + 1e-8), -np.pi, np.pi)
        return Z.astype(np.float32)
