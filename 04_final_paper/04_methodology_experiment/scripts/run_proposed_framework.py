from common import predict_proposed, write_predictions


def main() -> None:
    out_path = write_predictions("rag_docguard", predict_proposed)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
