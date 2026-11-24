from setuptools import setup, find_packages

setup(
    name="nexus-engine",
    version="0.3.0",
    description="Nexus Engine - Python game engine (Unity-inspired)",
    author="Nexus Engine Team",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=["pygame>=2.5.0", "numpy>=1.24.0"],
    extras_require={
        "3d": ["panda3d>=1.10.14", "ursina>=7.0.0"],
        "compute": ["taichi>=1.7.0"],
        "build": ["pyinstaller>=6.0.0"],
        "all": ["panda3d>=1.10.14", "ursina>=7.0.0", "taichi>=1.7.0", "pyinstaller>=6.0.0"],
    },
    entry_points={
        "console_scripts": [
            "nexus-build=nexus_engine.build.builder:main",
        ],
    },
)
