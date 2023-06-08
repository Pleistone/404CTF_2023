public function bf(){
    $host = 'challenges.404ctf.fr';
    $port = 31451;
    $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP) or die("Could not create socket\n");
    $result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");

    $buffer = '';
    while (strpos($buffer, 'message en clair :') === false) {
        $b = socket_read($socket, 1024);
        $buffer .= $b;
    }

    // $word = false;
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
    $buffer = '';
    while (strpos($buffer, 'message en clair :') === false) {
        $b = socket_read($socket, 4096);
        $buffer .= $b;
       // echo $b;
    }
    echo "return : ".strlen($buffer)."bytes...\n";
    $buffer = str_replace("message chiffre  :", '', $buffer);
    $buffer = trim($buffer);
    $tranches = str_split($buffer, 5);
    $encoded_array =  str_split($encoded, 5);

    foreach($encoded_array as $s){

        foreach ($tranches as $key => $tranche) {
            if ($tranche === $s) {
                echo "$s == ".substr($str,$key * 5, 5)."\n";
            }
        }

    }
}