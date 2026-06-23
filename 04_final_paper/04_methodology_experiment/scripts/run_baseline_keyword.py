from common import predict_keyword, write_predictions


def main() -> None:
    out_path = write_predictions("baseline_keyword", predict_keyword)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
