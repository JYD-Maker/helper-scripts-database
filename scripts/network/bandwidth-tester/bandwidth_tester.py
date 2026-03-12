import speedtest


def run_speed_test():
    """
    Runs an internet bandwidth test.
    """

    print("\nBandwidth Tester")
    print("-----------------------------")

    try:
        st = speedtest.Speedtest()

        print("Finding best server...")
        st.get_best_server()

        print("Testing download speed...")
        download_speed = st.download() / 1_000_000

        print("Testing upload speed...")
        upload_speed = st.upload() / 1_000_000

        print("\nResults")
        print("-----------------------------")
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed  : {upload_speed:.2f} Mbps")
        print("-----------------------------\n")

    except Exception as error:
        print("Error running speed test.")
        print(error)


if __name__ == "__main__":
    run_speed_test()
