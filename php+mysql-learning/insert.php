
<?php 

    include("mysql.php")	
       
    $name="xxx"
    $pwd="xxx"

	$con= mysqli_connect($myhost,$myuser,$mypw,$mydb) ; 

	if (mysqli_connect_errno($con))
	{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}

	$sql = "INSERT INTO student(name,password) VALUES ('$name','$pwd')" ; 

	mysqli_query($con,$sql);
    mysqli_close($con);

?>
