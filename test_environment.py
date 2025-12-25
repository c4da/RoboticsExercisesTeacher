"""
Test script to verify the robotics environment is set up correctly.
Run this script before starting the notebook to ensure all dependencies are installed.
"""

import sys

def test_imports():
    """Test if all required packages are available."""
    print("Testing package imports...\n")

    packages = {
        'numpy': None,
        'matplotlib': None,
        'mpl_toolkits.mplot3d': None,
        'matplotlib.widgets': None,
        'IPython.display': None
    }

    all_passed = True

    for package_name in packages:
        try:
            if '.' in package_name:
                parts = package_name.split('.')
                pkg = __import__(parts[0])
                for part in parts[1:]:
                    pkg = getattr(pkg, part)
            else:
                pkg = __import__(package_name)
            packages[package_name] = True
            print(f"✓ {package_name:30s} - OK")
        except ImportError as e:
            packages[package_name] = False
            all_passed = False
            print(f"✗ {package_name:30s} - FAILED")
            print(f"  Error: {e}")

    print("\n" + "="*60)
    if all_passed:
        print("✓ All packages installed correctly!")
        print("You can now run the forward_kinematics.ipynb notebook.")
    else:
        print("✗ Some packages are missing.")
        print("Please install requirements with: pip install -r requirements.txt")
    print("="*60)

    return all_passed

def test_basic_functionality():
    """Test basic numpy and matplotlib functionality."""
    print("\nTesting basic functionality...\n")

    try:
        import numpy as np

        # Test numpy
        arr = np.array([1, 2, 3])
        print(f"✓ NumPy array creation: {arr}")

        # Test matrix operations
        matrix = np.eye(3)
        print(f"✓ NumPy matrix operations: Identity matrix shape = {matrix.shape}")

        # Test trigonometric functions
        angle = np.pi / 4
        cos_val = np.cos(angle)
        print(f"✓ NumPy trigonometric functions: cos(45°) = {cos_val:.4f}")

        print("\n✓ Basic functionality test passed!")
        return True

    except Exception as e:
        print(f"\n✗ Basic functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("Robotics Environment Test")
    print("="*60)
    print()

    imports_ok = test_imports()

    if imports_ok:
        functionality_ok = test_basic_functionality()

        if functionality_ok:
            print("\n" + "="*60)
            print("All tests passed! Your environment is ready.")
            print("="*60)
            sys.exit(0)

    print("\n" + "="*60)
    print("Some tests failed. Please fix the issues above.")
    print("="*60)
    sys.exit(1)

