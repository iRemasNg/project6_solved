<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Times and APIs</title>

</head>

<body>

    <h2>List All Brevets</h2>
    <ul>
        <?php
        // Replace 'http://laptop-service/listAll' with the actual URL of your API endpoint
        $json = file_get_contents('http://laptop-service/listAll');
        $data = json_decode($json);

        foreach ($data->brevets as $brevet) {
            echo "<li>Distance: {$brevet->distance}</li>";
            echo "<li>Begin Date: {$brevet->begin_date}</li>";
            echo "<li>Begin Time: {$brevet->begin_time}</li>";
            echo "<ul>";

            foreach ($brevet->controls as $control) {
                echo "<li>KM: {$control->km}</li>";
                echo "<li>MI: {$control->mi}</li>";
                echo "<li>Location: {$control->location}</li>";
                echo "<li>Open: {$control->open}</li>";
                echo "<li>Close: {$control->close}</li>";
            }

            echo "</ul></li>";
        }
        ?>
    </ul>

    <h2>List Open Times</h2>
    <ul>
        <?php
        // Replace 'http://laptop-service/openOnly' with the actual URL of your OpenOnly API endpoint
        $json = file_get_contents('http://laptop-service/listOpenOnly');
        $data = json_decode($json);

        foreach ($data->brevets as $brevet) {
            echo "<li>Distance: {$brevet->distance}</li>";
            echo "<li>Begin Date: {$brevet->begin_date}</li>";
            echo "<li>Begin Time: {$brevet->begin_time}</li>";
            echo "<ul>";

            foreach ($brevet->controls as $control) {
                echo "<li>KM: {$control->km}</li>";
                echo "<li>MI: {$control->mi}</li>";
                echo "<li>Location: {$control->location}</li>";
                echo "<li>Open: {$control->open}</li>";
            }

            echo "</ul></li>";
        }
        ?>
    </ul>

    <h2>List Close Times</h2>
    <ul>
        <?php
        // Replace 'http://laptop-service/closeOnly' with the actual URL of your CloseOnly API endpoint
        $json = file_get_contents('http://laptop-service/listCloseOnly');
        $data = json_decode($json);

        foreach ($data->brevets as $brevet) {
            echo "<li>Distance: {$brevet->distance}</li>";
            echo "<li>Begin Date: {$brevet->begin_date}</li>";
            echo "<li>Begin Time: {$brevet->begin_time}</li>";
            echo "<ul>";

            foreach ($brevet->controls as $control) {
                echo "<li>KM: {$control->km}</li>";
                echo "<li>MI: {$control->mi}</li>";
                echo "<li>Location: {$control->location}</li>";
                echo "<li>Close: {$control->close}</li>";
            }

            echo "</ul></li>";
        }
        ?>
    </ul>

</body>

</html>

