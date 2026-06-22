import os
import subprocess
import sys


def run(cmd):
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return out.strip()
    except Exception as e:
        return f"FAILED: {e}"


def main():
    print("=== Python ===")
    print(sys.version)

    print("\n=== Environment ===")
    print("CUDA_VISIBLE_DEVICES:", os.environ.get("CUDA_VISIBLE_DEVICES", "<unset>"))
    print("NVIDIA_VISIBLE_DEVICES:", os.environ.get("NVIDIA_VISIBLE_DEVICES", "<unset>"))

    print("\n=== nvidia-smi ===")
    print(run(["nvidia-smi"]))

    print("\n=== PyTorch CUDA Check ===")
    try:
        import torch

        print("torch version:", torch.__version__)
        print("torch.version.cuda:", torch.version.cuda)
        print("cuda available:", torch.cuda.is_available())
        print("cuda device count:", torch.cuda.device_count())
        if torch.cuda.is_available():
            print("gpu name:", torch.cuda.get_device_name(0))
            x = torch.randn(1024, 1024, device="cuda")
            y = x @ x
            print("cuda tensor test:", float(y.mean().detach().cpu()))
        else:
            print("CUDA is not available inside PyTorch.")
    except Exception as e:
        print("PyTorch check failed:", repr(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
