<?php 
 
	include("mysql.php")
	$con= mysqli_connect($myhost,$myuser,$mypassw,$mybd) ; 
	
	if (mysqli_connect_errno($con))
	{
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
		
	$sql = "SELECT id ,name ,password FROM student " ; 

	$result=mysqli_query($con,$sql);

	while($row = mysqli_fetch_array($result)) {
		echo $row["id"] . "<br>";
		echo $row["name"] . "<br>"; 
		echo $row["password"] . "<br>";
	}
   mysqli_close($con);
?>