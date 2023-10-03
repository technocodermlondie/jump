  // Variables
var score = 0;
var lives = 10;

// Create Sprites
createEdgeSprites();

var platform1 = createSprite(100, 200);
platform1.setAnimation("platform");
platform1.velocityY = 2;

var platform2 = createSprite(300, 0);
platform2.setAnimation("platform");
platform2.velocityY = 2;

var carrot1 = createSprite(randomNumber(50, 350), 0);
carrot1.setAnimation("carrot");
carrot1.velocityY = 3;
carrot1.scale = 0.5;

var carrot2 = createSprite(randomNumber(50, 350), 0);
carrot2.setAnimation("carrot");
carrot2.velocityY = 3;
carrot2.scale = 0.5;

var Rock = createSprite(randomNumber(50, 350),-10);
Rock.setAnimation("Rock");
Rock.velocityY = 3;
Rock.scale = 0.2;

var player = createSprite(randomNumber(50, 350), 0);
player.setAnimation("playerR");
player.velocityY = 3;
player.scale = 0.5;

var GameOver = createSprite(200,200);
GameOver.setAnimation("Gameover");
GameOver.scale = 2;
GameOver.visible = false;

function draw() {
  // draw the background
  if (score > 24) {
    background2();
  } else {
    background1();
  }
  // update the sprites
  if (platform1.y > 410) {
    loopPlatform1();
  }
  
  if (player.y > 410) {
    deductLives();
    player.y = 200;
    player.x = 200;
    player.velocityY = 0;
    player.velocityX = 0;
  }
  
  if (player.y < -10) {
    deductLives();
    player.y = 200;
    player.x = 200;
    player.velocityY = 0;
  }
  
  if (player.x > 410) {
    deductLives();
    player.y = 200;
    player.x = 200;
    player.velocityX = 0;
  }
  
  if (player.x < -10) {
    deductLives();
    player.y = 200;
    player.x = 200;
    player.velocityX = 0;
  }
  
  if (platform2.y > 410) {
    loopPlatform2();
  }
  
  if (carrot1.y > 410) {
    loopItem1();
  }
  
  if (carrot2.y > 410) {
    loopItem2();
  }
  
  if (Rock.y > 550) {
    loopItem3();
  }
  
  if (Rock.isTouching(player)) {
    deductLives();
    loopItem3();
  }
  
  if (lives === 0) {
    gameOver();
  }
  
  controlPlayer();
  
  collectingItems();
  
  playerFall();
  
  playerLands();
  
  sideWalls();

  showScore();
  
  showLives();
  
  drawSprites();
}

// Functions
function background1() {
  background("Aqua");
  noStroke();
  fill("yellow");

  ellipse(340, 50, 60, 60);
}
function background2() {
    background("red");
  noStroke();
  fill("yellow");
  ellipse(340, 50, 60, 60);
}
function showScore() {
  fill("white");
  textSize(20);
  text("Score: ",10, 10, 80, 20);
  text(score, 70,10,80,20);
}

function showLives() {
  fill("white");
  textSize(20);
  text("Lives: ",310, 10, 80, 20);
  text(lives, 360,10,80,20);
}

function loopPlatform1() {
  platform1.y = -10;
}

function loopPlatform2() {
  platform2.y = -10;
}

function loopItem1() {
  carrot1.y = -10;
  carrot1.x = randomNumber(50,350);
}

function loopItem3() {
  Rock.y = -20;
  Rock.x = randomNumber(50,350);
}

function loopItem2() {
  carrot2.y = -10;
  carrot2.x = randomNumber(50,350);
}

function playerFall(){
  player.velocityY = player.velocityY + 0.2;
}

function controlPlayer(){
  if (keyWentDown("space")) {
      player.velocityY = player.velocityY - 10;
  }
  
  if (keyDown("left")) {
      player.velocityX = player.velocityX - 0.5;
      player.setAnimation("playerL");
  }
  
  if (keyDown("right")) {
      player.velocityX = player.velocityX + 0.5;
      player.setAnimation("playerR");
  }
}

function playerLands(){
  if (player.isTouching(platform1)) {
    player.collide(platform1);
  }
  
  if (player.isTouching(platform2)) {
    player.collide(platform2);
  }
  
}

function collectingItems(){
  if (player.isTouching(carrot1)) {
    score = score + 1;
    loopItem1();
  }
  
  if (player.isTouching(carrot2)) {
    score = score + 1;
    loopItem2();
  }
}

function deductLives() {
  lives = lives - 1;
}

function gameOver() {
  GameOver.visible = true;
}

function sideWalls() {
  player.collide(leftEdge);
  player.collide(rightEdge);
}