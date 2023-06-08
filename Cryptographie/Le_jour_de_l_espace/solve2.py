

"""
  $str = '';
            for ($i = 97; $i <= 121; $i++) {
                for ($j = 97; $j <= 121; $j++) {
                    for ($k = 97; $k <= 121; $k++) {
                        for ($l = 97; $l <= 121; $l++) {
                            for ($m = 97; $m <= 121; $m++) {
                                $word = chr($i) . chr($j) . chr($k) . chr($l).chr($m);
                                $str .= $word;
                            }
                        }
                    }
                }
            }

            $encoded = "ueomaspblbppadgidtfn";

            echo "sending :".strlen($str)." bytes...\n";
            socket_write($socket, $str . "\n");
"""