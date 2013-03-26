#!/bin/bash
./webqresp --repeat=3 --start=5 --response-seconds=1.5 --header='X-Name: Value' --content='{name: value}' --method=POST http://example.com/some/page
