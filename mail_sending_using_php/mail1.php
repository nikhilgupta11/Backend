<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;
require 'PHPMailer-master/PHPMailer-master/src/Exception.php';
require 'PHPMailer-master/PHPMailer-master/src/PHPMailer.php';
require 'PHPMailer-master/PHPMailer-master/src/SMTP.php';

$mail = new PHPMailer();
$mail->IsSMTP();

$mail->SMTPDebug  = 0;  
$mail->SMTPAuth   = TRUE;
$mail->SMTPSecure = "tls";
$mail->Port       = 587;
$mail->Host       = "smtp.gmail.com";
$mail->Username   = "nikhilgupta110299@gmail.com";
$mail->Password   = "ng11021999";

$mail->IsHTML(true);
$mail->AddAddress("jplksaini@gmail.com", "Lokesh KUmar Saini");
$mail->SetFrom("jplksaini@gmail.com", "Lokesh KUmar Saini");
$mail->AddReplyTo("jplksaini@gmail.com", "Lokesh KUmar Saini");
//$mail->AddCC("soumil.goyal@yahoo.com.sg", "Soumil Goyal");
$mail->Subject = "New Registration on Website!";
if (isset($_POST['submit'])) {

    $name = $_POST["name"];
    $email = $_POST["email"];
    $phonenumber = $_POST["phonenumber"];
    $howdidyouhear = $_POST["howdidyouhear"];
    $howmanymonths = $_POST["howmanymonths"];

    $finalmessage = "";

    $allanswers = array(
          "Full name" => $name,
           "Email address" => $email,
            "Phone number" => $phonenumber,
            "How did you hear about this workshop" => $howdidyouhear,
            "How many months are you signing for" => $howmanymonths,);

    foreach ($allanswers as $x => $value) {
        $finalmessage = $finalmessage . "$x is: $value<br>";
    }    

    echo "$finalmessage";
}

$content = "$finalmessage";

$mail->MsgHTML($content); 
if(!$mail->Send()) {
    echo "Error while sending Email.";
    var_dump($mail);
} else {
    echo "Email sent successfully";
} 
header("location: index.html")
?>