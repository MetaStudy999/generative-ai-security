from common import predict_no_filter, write_predictions


def main() -> None:
    out_path = write_predictions("baseline_no_filter", predict_no_filter)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
