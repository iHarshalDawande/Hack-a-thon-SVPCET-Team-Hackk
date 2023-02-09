/**
 *
 *You cannot sign up for this service with a gmail address
 *
 */

let email = "example@abcd.com";

let isGmailAddress = email.includes("@gmail.com");

if (isGmailAddress) {
  console.log("Sorry, you cannot sign up with a @gmail.com adress");
} else {
  console.log("this is not a gmail address.so it is ok");
}
