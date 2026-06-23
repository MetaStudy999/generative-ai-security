from common import predict_regex, write_predictions


def main() -> None:
    out_path = write_predictions("baseline_regex", predict_regex)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
