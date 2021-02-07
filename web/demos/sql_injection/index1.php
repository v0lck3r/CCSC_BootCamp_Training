<?php
	$mysqli = new mysqli("localhost","root","root","cit");

	// Check connection
	if ($mysqli -> connect_errno) {
  	print("Failed to connect to MySQL: " . $mysqli -> connect_error);
  	exit();
	}

    $username = $_GET['username'];
    $result = mysqli_query($mysqli,"SELECT * FROM user WHERE username='$username'");
    while($row = mysqli_fetch_array($result))
     {
        print_r($row);
     }
?>
