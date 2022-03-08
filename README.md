# Fenix Blockchain Pipeline Demo

This is a simple demo of using the Fenix Blockchain SDK. It only requires `make` and `docker`.

**Note:** Windows users will need to install make; the easiest way to do this is with [Chocolatey](https://chocolatey.org/) and `choco install make`.

## Environment

You must set a single environment variable for this to work - create a file in root directory called `.envrc` or `.env` if you're not using pyenv

```sh
export FENIX_API_KEY=<key assigned by your representative>
```

## Build

Then you can build project's container by running `make build`:

```sh
$ make build
docker build --force-rm . --tag fenix-sdk-demo
[+] Building 0.8s (7/7) FINISHED
 => <snipped output>

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

## Run

Run the demo using `make run`:

```sh
$ make run
docker run --rm -v /Users/seawolf/repos/fenix/fenix-sdk-demo/:/usr/demo -e FENIX_API_KEY -ti fenix-sdk-demo python -m demo
connecting to: wss://api.fenixblockchain.com/ws
subscribing: TRADES_BY_MARKET/btc-usdt
other message: {'type': 'subscribed', 'message': 'trades/market/btc-usdt'}
received: Trade(id=huobi:btc-usdt:102534818156, timestamp=1632606055.447, exchange=huobi, pair=btc-usdt, euid=102534818156, price=42563.71, quantity=0.000395, direction=sell)
received: Trade(id=binance:btc-usdt:1068723019, timestamp=1632606055.335, exchange=binance, pair=btc-usdt, euid=1068723019, price=42562.77, quantity=0.00118, direction=buy)
received: Trade(id=binance:btc-usdt:1068723020, timestamp=1632606055.353, exchange=binance, pair=btc-usdt, euid=1068723020, price=42562.45, quantity=0.00039, direction=sell)
... <output snipped> ...
other message: {'type': 'unsubscribed', 'message': 'trades/market/btc-usdt'}
receive loop stopped
disconnecting from: wss://api.fenixblockchain.com/ws
```

## Cleanup

To clean up docker resources, use `make clean`:

```sh
$ make clean
rm -rf __pycache__
docker rmi fenix-sdk-demo
Untagged: fenix-sdk-demo:latest
Deleted: sha256:9b7812d65639553a442c4a0324ff07868142f16b1ea647e2e0bd4fa93b058441
```

Everything else can be cleaned up by simply deleting this folder.
