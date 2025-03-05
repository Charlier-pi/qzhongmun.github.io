React:

npx create-react-app@latest {project name}

hooks
figma
Basics: HTML,CSS,Javascript,cs6
JSX

https://reactjs.org/docs/cdn-links.html
https://reactjs.org/docs/add-react-to-a-website.html#quickly-try-jsx

Create index.js index.html index.css
python -m http.server
visit http://localhost:8000/

ReactDOM.render(<h1>Hello, everyone!</h1>, document.getElementById("root"))
function MainContent() {return <h1>I'm learning React!</h1>;}
ReactDOM.render(<div><MainContent /></div>,document.getElementById("root"));

npx create-react-app@latest {project name}
cd {project name}
npm start

---

CSS:
framework:
https://nextjs.org/
https://www.gatsbyjs.com/

padding: 30px 25px; top-bottom:30px, left-right padding:25px 这个不能用在主页面上，要不布局不齐
justify-content: space-between;
align-items: center;
font-weight: 600; 字体粗细
font-size: 22px; 字体大小
letter-spacing: -0.05em; 修改字体中间的距离
line-height: 19px; 修改字体高度
padding-block: 10px; 修改行之间的距离
max-width: 400px; 字段最大宽度
max-width: 100px; 解决图片最大宽度
text-align: justify; 文本左右齐
margin-right: auto; 文字自动靠右
text-indent: 5px; 文本前留空隙

<p><span className="bold">From $136</span> / person</p>   部分文字变成粗体 .bold{ font-weight: bold;}
https://developer.mozilla.org/en-US/docs/Web/CSS/::marker  maker 修改

<div className="Group">{DataElement}</div>          // 让模块并列排，可滑动
.Group {
  display: flex;
  flex-wrap: nowrap;
  gap: 20px;
  overflow-x: auto;
}
.整个模块{
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
}

align-items: center; //垂直居中

2 个 buttons 水平居中，放在总 classname 里面
display: flex;
justify-content: space-between; or center

display: flex; //水平居中
align-items: center;

body {
min-height: 100vh;
display: flex; //水平 垂直居中
justify-content: center;  
 align-items: center;
}

text-align: center;
vertical-align: middle;
line-height: 90px; //水平 垂直居中 最新，line-height 于所在 div 高度一致

- {
  box-sizing: border-box; //1
  }

body {
margin: 0;
background-color: #0b2434; //2 , html automatically have body elements important  
 padding: 20px;
}

export const Main = styled.div`           //3: 1-3 shows two box, one inside another one
  background-color: #f5f5f5;
  border-radius: 5px;
  height: 90vh;
  text-align: center;`;

main {
display: flex;
flex-direction: column; //column 垂直居中从上到下 column 间间距小
justify-content: center;
align-items: center;
}

grid:
display: grid;
grid-template: auto auto / repeat(5, 1fr); or grid-template-columns: auto auto auto auto auto; //important

.box {
height: 100px; //important number inside this box will center horizontally and vertically
width: 100px;
border: 1px solid black;
display: inline-block;
margin-right: 4px;
border-radius: 5px;
text-align: center; //important
vertical-align: middle; //important
line-height: 100px; //important
}

height: 100px;
width: 100px;
border: 1px solid black; //square shape
display: inline-block; // display inline

set background picture:
main{
background-image: url(./images/reactjs-icon.png);
background-repeat: no-repeat;
background-position: right 50%;
background-size: cover; 背景图片占满整个容器
body {
background: #282d35;
}

---

Html:

<hr /> 换行

---

JSX：
{Javascript}
{props.setup && <h3>Setup: {props.setup}</h3>} // 如果存在 setup，然后才显示 setup

 <h3 style={{display: props.setup ? "block" : "none"}}>Setup: {props.setup}</h3>    // 如果存在setup，然后才显示setup
src={`../images/${props.img}`}

Get data from hard writing:
Props input: <Contact img="./images/pumpkin.png"/>
Props output: export default function Contact(props) {return ( <img src={props.img}/>)}

Get data from file:
Props input:
import jokesData from "./jokesData"
export default function App() {
const jokeElements = jokesData.map(joke => {return <Joke setup={joke.setup} punchline="joke.punchline" /> })
Props output: <div>{jokeElements}</div>

{props.openSpots === 0 && <div className="soldout">SOLD OUT</div>} //一样的意思
{!props.openSpots && <div className="soldout">SOLD OUT</div>} //一样的意思

input:
import Data from "./Data";
export default function App() {
const DataElement = Data.map((x) => (

<Footer
      key={x.id}
      item={x}
    />
));
output: src={`../images/${props.item.coverImg}`}

input:
import Data from "./Data";
export default function App() {
const DataElement = Data.map((x) => (

<Footer
key={x.id}
{...x}
/>
));
output: src={`../images/${props.coverImg}`}

---

## Program1:

/\*
Challenge - recreate the above line of code in vanilla JS by creating and
appending an h1 to our div#root (without using innerHTML).

- Create a new h1 element
- Give it some textContent
- Give it a class name of "header"
- append it as a child of the div#root

\*/
var s = document.getElementById('root');

function myFunction(text) {
var h = document.createElement("H1");
var t = document.createTextNode(text);
h.appendChild(t);
document.body.appendChild(h);
}
ReactDOM.render(myFunction('231'),s)

Ture answers are here:
const h1 = document.createElement("h1")
h1.textContent = "This is an imperative way to program"
h1.className = "header"
document.getElementById("root").append(h1)

---

// JSX
ReactDOM.render(

<div>
<h1 className="header">This is JSX</h1>
<p>This is a paragraph</p>
</div>,
document.getElementById("root")
)

---

import React from "react"
import ReactDOM from "react-dom"
instead of <script crossorigin src="https://unpkg.com/react@17/umd/react.development.js"></script>

---

Quize:

1. Why do we need to `import React from "react"` in our files?
   React is what defines JSX

2. If I were to console.log(page) in index.js, what would show up?
   A JavaScript object. React elements that describe what React should eventually add to the real DOM for us.

3. What's wrong with this code:

```
const page = (
    <h1>Hello</h1>
    <p>This is my website!</p>
)
```

We need our JSX to be nested under a single parent element

4. What does it mean for something to be "declarative" instead of "imperative"?
   Declarative means I can tell the computer WHAT to do and expect it to handle the details.
   Imperative means I need to tell it HOW to do each step.

5. What does it mean for something to be "composable"?
   We have small pieces that we can put together to make something larger/greater than the individual pieces.

---

## Custom Components:

import React from "react"
import ReactDOM from "react-dom"

function TemporaryName() {
return (

<div>
<img src="./react-logo.png" width="40px" />
<h1>Fun facts about React</h1>
<ul>
<li>Was first released in 2013</li>
<li>Was originally created by Jordan Walke</li>
<li>Has well over 100K stars on GitHub</li>
<li>Is maintained by Facebook</li>
<li>Powers thousands of enterprise apps, including mobile apps</li>
</ul>
</div>
)
}
ReactDOM.render(<TemporaryName />, document.getElementById("root"))

---

import React from "react"
import ReactDOM from "react-dom"

function Page() {
return (

<div>
<header>
<nav>
<img src="./react-logo.png" width="40px" />
</nav>
</header>
<h1>Reasons I'm excited to learn React</h1>
<ol>
<li>It's a popular library, so I'll be
able to fit in with the cool kids!</li>
<li>I'm more likely to get a job as a developer
if I know React</li>
</ol>
<footer>
<small>© 2021 Ziroll development. All rights reserved.</small>
</footer>
</div>
)
}

## ReactDOM.render(<Page />, document.getElementById("root"))

Quiz:

1. What is a React component?
   A function that returns React elements. (UI), it is reusable

2. What's wrong with this code?

```
function myComponent() {
    return (
        <small>I'm tiny text!</small>
    )
}
```

MyComponent()

3. What's wrong with this code?

```
function Header() {
    return (
        <header>
            <nav>
                <img src="./react-logo.png" width="40px" />
            </nav>
        </header>
    )
}

ReactDOM.render(Header(), document.getElementById("root"))
```

## <Header />

Child and Parent(Page()) Component:

import React from "react"
import ReactDOM from "react-dom"

/\*\*
Challenge:

- Move the `footer` into its own component called "Footer"
  and render that component inside the Page component.
- Move the `h1` and `ol` together into another component
  called "MainContent" and render inside Page as well.
  \*/

function Header() {
return (

<header>
<nav>
<img src="./react-logo.png" width="40px" />
</nav>
</header>
)
}

function Footer() {
return (

<footer>
<small>© 2021 Ziroll development. All rights reserved.</small>
</footer>
)
}

function MainContent() {
return (

<div>
<h1>Reasons I'm excited to learn React</h1>
<ol>
<li>It's a popular library, so I'll be
able to fit in with the cool kids!</li>
<li>I'm more likely to get a job as a developer
if I know React</li>
</ol>
</div>
)
}

function Page() {
return (

<div>
<Header />
<MainContent />
<Footer />
</div>
)
}

## ReactDOM.render(<Page />, document.getElementById("root"))

css:
.nav {
display: flex;
justify-content: space-between;
align-items: center;
}

.nav-logo {
width: 60px;
}

.nav-items {
list-style: none;
display: flex;
}

.nav-items > li {
padding: 10px;
}

index.js
import React from "react"
import ReactDOM from "react-dom"

/\*\*
Challenge:

- Add an `ul` inside the Header's `nav` and create
  the following `li`s: "Pricing", "About", & "Contact"
- Using flexbox, line up the nav items horizontally, and
  put them inline with the React logo.
- Change the image styling to happen in CSS instead of in-line
  For practice, add a new class to the image in order to style it
  \*/

function Header() {
return (

<header>
<nav className="nav">
<img src="./react-logo.png" className="nav-logo" />
<ul className="nav-items">
<li>Pricing</li>
<li>About</li>
<li>Contact</li>
</ul>
</nav>
</header>
)
}

function Footer() {
return (

<footer>
<small>© 2021 Ziroll development. All rights reserved.</small>
</footer>
)
}

function MainContent() {
return (

<div>
<h1>Reasons I'm excited to learn React</h1>
<ol>
<li>It's a popular library, so I'll be
able to fit in with the cool kids!</li>
<li>I'm more likely to get a job as a developer
if I know React</li>
</ol>
</div>
)
}

function Page() {
return (

<div>
<Header />
<MainContent />
<Footer />
</div>
)
}

## ReactDOM.render(<Page />, document.getElementById("root"))

Footer.js:
import React from "react";
export default function Footer() {
return (

<footer>
<small>© 2021 Ziroll development. All rights reserved.</small>
</footer>
)
}

Main.js:
import Header from "./Header"

---

Set up a local react environment with create react app:
Check for "node -v" and "npm -v"
npx create-react-app@latest {project name}
cd {project name}
npm start

https://elemefe.github.io/element-react/#/zh-CN/time-picker
https://www.amcharts.com/demos/
Free fonts style:
https://fonts.google.com/
CSS style:
https://developer.mozilla.org/en-US/docs/Web/CSS/::marker

how to change font in css:
body{
font-family: "Karla", sans-serif; //1
}

.div{
font-family: "Karla", sans-serif; //2 1+2 done
}

---

start a new program app2
npx create-react-app@latest app2
cd app2
npm start

detele docs in /src and
add folders: components(里面的文件名必须大写开头), images
add files: App.css, App.js, index.js

---

Git:

git init
git remote add origin [url]
git fetch origin main
git checkout -b main origin/main
# Make changes
git add .
git commit -m 'your message'
git push origin main

git init
git remote add origin url
git pull origin main

git pull --rebase origin main
git push --set-upstream origin main

git remote add master url
git pull
git —version
Git stash
git clone url
git branch -M master
git checkout master
git remote remove origin //delete existed .git

git add .
git commit -m 'your message'
git push
git push origin master

git remote -v
git branch
git add .
git commit -m "new commit"
git push origin master
git remote -v
git remote origin set-url https://github.com/qzhongmun/React_Pros.git
git remote set-url origin https://github.com/qzhongmun/React_Pros.git
git push origin master

git init
git clone url
git add .
git commit -m 'your message'
git remote add origin url
git push
git push --set-upstream origin master

---

2. Data driven React:
   props
   creating omponents from an array

import React from "react"
import ReactDOM from "react-dom"

function App() {
const date = new Date() //logic part
const hours = date.getHours()
let timeOfDay

    if (hours < 12) {
        timeOfDay = "morning"
    } else if (hours >= 12 && hours < 17) {
        timeOfDay = "afternoon"
    } else {
        timeOfDay = "night"
    }                          //logic part

    return (
        <h1>Good {timeOfDay}!</h1>   //display part     it is JSX: <h1>Good {timeOfDay}!</h1>  inside{}is JavaScript
    )

}

HTML:
<input placeholder="First Name" /> => input
<input placeholder="First Name" type="submit" /> => bottom
<input placeholder="First Name" type="radio" /> => checkbox

---

props:
import React from "react"
import Contact from "./Contact"

export default function App() {
return (

<div className="contacts">
<Contact 
                img="./images/mr-whiskerson.png" 
                name="Mr. Whiskerson"
                phone="(212) 555-1234"
                email="mr.whiskaz@catnap.meow"
            />
<Contact 
                img="./images/fluffykins.png"
                name="Fluffykins"
                phone="(212) 555-2345"
                email="fluff@me.com"
            />
<Contact 
                img="./images/felix.png"
                name="Felix"
                phone="(212) 555-4567"
                email="thecat@hotmail.com"
            />
<Contact 
                img="./images/pumpkin.png"
                name="Pumpkin"
                phone="(0800) CAT KING"
                email="pumpkin@scrimba.com"
            />
</div>
)
}

import React from "react"
export default function Contact(props) {
/\*\*
_ Challenge: Fix the code below to use the `props`
_ object values in place of the hardcoded values below
\*/
return (

<div className="contact-card">
<img src={props.img}/>
<h3>{props.name}</h3>
<div className="info-group">
<img src="./images/phone-icon.png" />
<p>{props.phone}</p>
</div>
<div className="info-group">
<img src="./images/mail-icon.png" />
<p>{props.email}</p>
</div>
</div>
)
}

/\*
{
img: "./images/mr-whiskerson.png",
name: "Mr. Whiskerson",
phone: "(212) 555-1234",
email: "mr.whiskaz@catnap.meow"
}

## \*/

Quiz:

1. What do props help us accomplish?
   Make a component more reusable.

2. How do you pass a prop into a component?
   <MyAwesomeHeader title="???" />

3. Can I pass a custom prop (e.g. `blahblahblah={true}`) to a native
   DOM element? (e.g. <div blahblahblah={true}>) Why or why not?
   No, because the JSX we use to describe native DOM elements will
   be turned into REAL DOM elements by React. And real DOM elements
   only have the properties/attributes specified in the HTML specification.
   (Which doesn't include properties like `blahblahblah`)

4. How do I receive props in a component?
   function Navbar(props) {
   console.log(props.blahblahblah)
   return (
   <header>
   ...
   </header>
   )
   }

5. What data type is `props` when the component receives it?
   An object!

---

export default function Contact({img, name, phone, email}) {
return (

<div className="contact-card">
<img src={img}/>
<h3>{name}</h3>
<div className="info-group">
<img src="./images/phone-icon.png" />
<p>{phone}</p>
</div>
<div className="info-group">
<img src="./images/mail-icon.png" />
<p>{email}</p>
</div>
</div>
)
}

---

Props: passing in non-string props
Bool: isPun={true}
number: upvotes={10}
list: comments={[{author: "", body: "", title: ""}, {...}]}

---

map()

const squares = nums.map(function(num) {
return num \* num
})

const capitalized = names.map((name) => {
return name[0].toUpperCase() + name.slice(1)
})

const paragraphs = pokemon.map(mon => `<p>${mon}</p>`)

## const squares = nums.map( x => x \* x)

export default function App() {
const colors = [

<h3>Red</h3>,
<h3>Orange</h3>,
<h3>Yellow</h3>,
<h3>Green</h3>,
<h3>Blue</h3>,
<h3>Indigo</h3>,
<h3>Violet</h3>
]
return (
<div>
{colors}
</div>
)
}

---

Map Quiz:

1. What does the `.map()` array method do?
   Returns a new array. Whatever gets returned from the callback
   function provided is placed at the same index in the new array.
   Usually we take the items from the original array and modify them
   in some way.

2. What do we usually use `.map()` for in React?
   Convert an array of raw data into an array of JSX elements
   that can be displayed on the page.

3. Why is using `.map()` better than just creating the components
   manually by typing them out?
   It makes our code more "self-sustaining" - not requiring
   additional changes whenever the data changes.

for(let i = 0; i < someArray.length; i++) {

## }

If picture can't display, put images file into public file, pictures will show
src={require("../images/react-icon-small.png")}

---

Dynamic web app:
Event listeners
State
Conditional rendering
Forms
Side effects

---

Header CSS:

- {
  box-sizing: border-box;
  }

body {
font-family: "Karla", sans-serif;
margin: 0;
}

.header {
display: flex;
align-items: center;
height: 65px;
background: linear-gradient(90deg, #672280 1.18%, #A626D3 100%);
color: white;
padding: 20px;
}

.header--image {
height: 100%;
margin-right: 6px;
}

.header--title {
font-size: 1.25rem;
margin-right: auto;
}

.header--project {
font-size: 0.75rem;
font-weight: 500;
}

---

Html + Css:

    <main>
      <form className="form">
        <input type="text" placeholder="Top text" className="form--input" />
        <input type="text" placeholder="Bottom text" className="form--input" />
        <button className="form--button">Get a new meme image 🖼</button>
      </form>
    </main>

.form {
display: grid;
grid-template: 40px 40px / 1fr 1fr;
gap: 17px;
}
.form--button {
grid-column: 1 / -1; //width=100%
}

---

Listener:
https://reactjs.org/docs/events.html#mouse-events

export default function App() {
function handleClick() {
console.log("I was clicked!")
}

    function handleOnMouseOver() {
        console.log("MouseOver")
    }

    return (
        <div className="container">
            <img
                src="https://picsum.photos/640/360"
                onMouseOver={handleOnMouseOver}
            />
            <button onClick={handleClick}>Click me</button>
        </div>
    )

}

---

const [things, setThings] = React.useState([]);
let url;
function addItem() {
const memesArray = memesData.data.memes;
const randomNumber = Math.floor(Math.random() \* memesArray.length);
url = memesArray[randomNumber].url;
const newThingText = url;
// setThings((prevState) => [...prevState, newThingText]); 重复增加
setThings((prevState) => [newThingText]); //只增加一次
}

const thingsElements = things.map((thing) => (
<img key={thing} src={thing} className="img1" />
));

return (
<button className="form--button" onClick={addItem}>Get a new meme image 🖼</button>
{thingsElements}
);
}

---

<Navbar darkMode={true} coverImage="some-image2" /> darkmode and lightmode ???

Props: imutable
State: will change the value

---

states:

import React from "react";
import ReactDOM from "react-dom";

function APP(){
const [users, setUsers] = React.useState([]);

    function greeting(name) {
    const date = new Date()
    const hours = date.getHours()
    let timeOfDay
    if(hours >= 4 && hours < 12) {
        timeOfDay = "morning"
    } else if(hours >= 12 && hours < 17) {
        timeOfDay = "afternoon"
    } else if(hours >= 17 && hours < 20) {
        timeOfDay = "evening"
    } else {
        timeOfDay = "night"
    }
    const newUser = `Good ${timeOfDay}, ${name}!`
    setUsers((prevState) => [newUser]);

}

const thingsElements = users.map((a) => (

<p>{a}</p>
));

return(

<div>
<button onClick={() => greeting("bob1")}> hi</button>
{thingsElements}
</div>
);
}

ReactDOM.render(<APP />, document.getElementById("root"))

---

Quiz for state and props:

1. How would you describe the concept of "state"?
   A way for React to remember saved values from within a component.
   This is similar to declaring variables from within a component,
   with a few added bonuses (which we'll get to later)

2. When would you want to use props instead of state?
   Anytime you want to pass data into a component so that
   component can determine what will get displayed on the
   screen.

3. When would you want to use state instead of props?
   Anytime you want a component to maintain some values from
   within the component. (And "remember" those values even
   when React re-renders the component).

4. What does "immutable" mean? Are props immutable? Is state immutable?
   Unchanging. Props are immutable. State is mutable.

---

React Hooks:

1. useState()
   import React, {useState} from "react" //or
   React.useState()

destructure useState:
const [isImportant, setIsImportant] = React.useState("Yes")

const [count, setCount] = React.useState(0)  
function add() {
setCount(count + 1) // equal to count++  
 //这个地方最好用 call back：setCount(preCount => preCount+1) or setCount(function(oldValue) { return oldValue + 1 })  
}

1.         setBoxs((oldNotes) =>
        oldNotes.map((oldNote) => {
          return oldNote.type ? { ...oldNote, value: getRandomInt() } : oldNote;     //1 simple
        })

    );

2.          setBoxs((oldNotes) => {
        return oldNotes.map((oldNote) => {
          return oldNote.type ? { ...oldNote, value: getRandomInt() } : oldNote;      //2 complex  1 and 2 are same function
        });
    });

---

State:

import React from "react"
export default function App() {
const result = React.useState("Yes")
console.log(result)
return (

<div className="state">
<h1 className="state--title">Is state important to know?</h1>
<div className="state--value">
<h1>{result[0]}</h1>
</div>
</div>
)
}

---

state:

import React from "react"

export default function App() {
const [isImportant, setIsImportant] = React.useState("Yes")
function handleClick() {
setIsImportant("No")
}

    return (
        <div className="state">
            <h1 className="state--title">Is state important to know?</h1>
            <div className="state--value" onClick={handleClick}>
                <h1>{isImportant}</h1>
            </div>
        </div>
    )

## }

useState:

import React from "react"

export default function App() {
const [count, setCount] = React.useState(0)  
 function add() {
setCount(count + 1) // equal to count++  
 //这个地方最好用 call back：setCount(preCount => preCount+1) or setCount(function(oldValue) { return oldValue + 1 })  
 }

    function subtract() {
        setCount(count - 1)
    }
    return (
        <div className="counter">
            <button className="counter--minus" onClick={subtract}>–</button>
            <div className="counter--count">
                <h1>{count}</h1>
            </div>
            <button className="counter--plus" onClick={add}>+</button>
        </div>
    )

}

css:

- {
  box-sizing: border-box;
  }

body {
margin: 0;
font-family: 'Inter', sans-serif;
background-color: #262626;
color: #D9D9D9;
padding: 20px;
height: 100vh;
display: flex;
justify-content: center;
align-items: center;
}

.counter {
display: flex;
align-items: flex-end;
}

.counter > button {
height: 50px;
width: 50px;
border-radius: 50%;
border: none;
cursor: pointer;
background-color: #737373;
color: #D9D9D9;
font-size: 1.5rem;
}

.counter > button:hover {
background-color: #404040;
color: #D9D9D9;
}

.counter > button:focus {
outline: none;
}

.counter--count {
background-color: white;
height: 100px;
width: 100px;
border-radius: 50%;
display: flex;
justify-content: center;
align-items: center;
color: #262626;
}

.counter--plus {
margin-left: -20px;
}

.counter--minus {
margin-right: -20px;
z-index: 1;
}

---

Quiz2: useState:

1. You have 2 options for what you can pass in to a
   state setter function (e.g. `setCount`). What are they?

a. New value of state (setCount(42))
b. Callback function - whatever the callback function
returns === new value of state

2. When would you want to pass the first option (from answer
   above) to the state setter function?
   Whenever you don't need the previous value of state to determine
   what the new value of state should be.

3. When would you want to pass the second option (from answer
   above) to the state setter function?
   Whenever you DO need the previous value to determine the new value

---

useState: 用此方法，修改后自动更新
export default function Meme() {
const [isImportant, setIsImportant] = React.useState("https://i.imgflip.com/30b1gx.jpg");
function getMemeImage() {
const memesArray = memesData.data.memes
const randomNumber = Math.floor(Math.random() \* memesArray.length)
setIsImportant(memesArray[randomNumber].url)
}
return (
<button 
                    className="form--button"
                    onClick={getMemeImage}
                >
Get a new meme image 🖼
</button>
<img className="img2" src={isImportant}></img>
)
}

---

ternary：
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
condition ? exprIfTrue : exprIfFalse

let answer = isGoingOut === true ? "Yes" : "No" /or below

const isGoingOut = false /or below
let answer = isGoingOut ? "Yes" : "No"

const isGoingOut = false
return (

<div className="state">
<h1 className="state--title">Do I feel like going out tonight?</h1>
<div className="state--value">
<h1>{isGoingOut ? "Yes" : "No"}</h1>
</div>
</div>
)

---

useState: 通过点击 Yes/No 连续变化
export default function App() {
const [isGoingOut,setIsGoingOut] = React.useState(true)
const [isGoing,setIsGoing] = React.useState("Yes")
function handleGoing(){
isGoingOut ? setIsGoing("No") : setIsGoing("Yes")
setIsGoingOut(!isGoingOut)
}
return (

<div className="state--value" onClick={handleGoing}>
<h1>{isGoing}</h1>
</div>
)
}

updated code:
export default function App() {
const [isGoingOut, setIsGoingOut] = React.useState(true)
function changeMind() {
setIsGoingOut(prevState => !prevState)
}
return (

<div onClick={changeMind} className="state--value">
<h1>{isGoingOut ? "Yes" : "No"}</h1>
</div>)}

---

useState: Add pages
function App() {
const [thingsArray,setThingsArray] = React.useState(["Thing 1", "Thing 2"])
function addItem() {
setThingsArray(predata =>[...predata,`Thing ${predata.length + 1}`])
}
const thingsElements = thingsArray.map(thing => <p key={thing}>{thing}</p>)
return (

<div>
<button onClick={addItem}>Add Item</button>
{thingsElements}
</div>
)
}
ReactDOM.render(<App />, document.getElementById('root'));

---

useState + CSS : Card
export default function App() {
const [contact, setContact] = React.useState({
firstName: "John",
lastName: "Doe",
phone: "+1 (719) 555-1212",
email: "itsmyrealname@example.com",
isFavorite: true
})

    let starIcon = contact.isFavorite ? "star-filled.png" : "star-empty.png"

    function toggleFavorite() {
        console.log("Toggle Favorite")
    }

    return (
        <main>
            <article className="card">
                <img src="./images/user.png" className="card--image" />
                <div className="card--info">
                    <img
                        src={`../images/${starIcon}`}
                        className="card--favorite"
                        onClick={toggleFavorite}
                    />
                    <h2 className="card--name">
                        {contact.firstName} {contact.lastName}
                    </h2>
                    <p className="card--contact">{contact.phone}</p>
                    <p className="card--contact">{contact.email}</p>
                </div>

            </article>
        </main>
    )

}

CSS:

- {
  box-sizing: border-box;
  }

body {
background-color: whitesmoke;
margin: 0;
font-family: "Inter", sans-serif;
}

main {
height: 100vh;
display: flex;
justify-content: center;
align-items: center;
}

.card {
width: 200px;
border: 1px solid lightgray;
border-radius: 10px;
height: 350px;
box-shadow: 5px 5px 5px 1px rgba(120,120,120,0.44);
-webkit-box-shadow: 5px 5px 5px 1px rgba(120,120,120,0.44);
-moz-box-shadow: 5px 5px 5px 1px rgba(120,120,120,0.44);
}

.card--image {
width: 100%;
padding: 10%;
padding-bottom: 0;
}

.card--name {
margin-block: 13px;
color: #333333;
}

.card--info {
padding: 10px;
}

.card--favorite {
width: 25px;
cursor: pointer;
}

.card--contact {
font-size: 0.75rem;
color: gray;
margin-block: 7px;
}

---

useState: only change part of it

const [contact, setContact] = React.useState({
firstName: "John",
lastName: "Doe",
phone: "+1 (719) 555-1212",
email: "itsmyrealname@example.com",
isFavorite: true
})

function toggleFavorite() {
setContact(prevContact => {
return {
...prevContact, //important
isFavorite: !prevContact.isFavorite //only change this one
}
})
}

or
setContact(prevContact => ({
...prevContact,
isFavorite: !prevContact.isFavorite //(include object)
}))

---

react will automatically update when you change the components, it is wonderful

APP.js
import React from "react"
import Count from "./Count"
export default function App() {
const [count, setCount] = React.useState(0)

    function add() {
        setCount(prevCount => prevCount + 1)
    }

    function subtract() {
        setCount(prevCount => prevCount - 1)
    }

    console.log("App component rendered")

    return (
        <div className="counter">
            <button className="counter--minus" onClick={subtract}>–</button>
            <Count number={count} />
            <button className="counter--plus" onClick={add}>+</button>
        </div>
    )

}

Count.js
import React from "react"
export default function Count(props) {
console.log("Count component rendered")

    return (
        <div className="counter--count">
            <h1>{props.number}</h1>
        </div>
    )

}

---

Setting state from child components

App.js (parent)
import React from "react"
import Star from "./Star"
export default function App() {
const [contact, setContact] = React.useState({
firstName: "John",
lastName: "Doe",
phone: "+1 (719) 555-1212",
email: "itsmyrealname@example.com",
isFavorite: true
})
function toggleFavorite() {
setContact(prevContact => ({
...prevContact,
isFavorite: !prevContact.isFavorite
}))
}  
 return (

<main>
<article className="card">
<img src="./images/user.png" className="card--image" />
<div className="card--info">
<Star isFilled={contact.isFavorite} handleClick={toggleFavorite} />
<h2 className="card--name">
{contact.firstName} {contact.lastName}
</h2>
<p className="card--contact">{contact.phone}</p>
<p className="card--contact">{contact.email}</p>
</div>

            </article>
        </main>
    )

}

Star.js (Child)
import React from "react"
export default function Star(props) {
const starIcon = props.isFilled ? "star-filled.png" : "star-empty.png"
return (
<img
src={`../images/${starIcon}`}
className="card--favorite"
onClick={props.handleClick}
/>
)
}

---

Passing data to components: sibling can't pass data, we have to move data to parent, then sibling can share the data

App.js Parent:
import React from "react"
import Header from "./Header"
import Body from "./Body"
export default function App() {
const [user, setUser] = React.useState("Joe1")
return (

<main>
<Header name={user}/>
<Body name={user}/>
</main>
)
}

Header.js Child1:
import React from "react"
export default function Header(props) {
return (

<header>
<p>Current user: {props.name}</p>
</header>
)
}

Body.js Child2:
import React from "react"
export default function Body(props) {
return (

<section>
<h1>Welcome back, {props.name}!</h1>
</section>
)
}

---

Dynamic Styles:

index.js
import React from "react"
import ReactDOM from "react-dom"
import App from "./App"
ReactDOM.render(<App darkMode={false} />, document.getElementById("root"))

App.js
import React from "react"
import boxes from "./boxes"
export default function App(props) {
const [squares, setSquares] = React.useState(boxes)
const styles = {
backgroundColor: props.darkMode ? "#222222" : "#cccccc"
}  
 const squareElements = squares.map(square => (

<div style={styles} className="box" key={square.id}></div> //it is important here, we can use {{backgroundColor: props.darkMode ? "#222222" : "#cccccc"}} too
))
return (
<main>
{squareElements}
</main>
)
}

---

import React from "react"
import boxes from "./boxes"
import Box from "./Box"
export default function App() {
const [squares, setSquares] = React.useState(boxes)
const squareElements = squares.map(square => (
<Box key={square.id} on={square.on} /> //have to include key, or err, but can't have onClick listeners, it won't work. but onclike works in div,h1...begin with lower words
))  
 return (

<main>
{squareElements}
</main>
)
}

---

Boxes Change: it is too complicate, we have to state at app.js and box.js
App.js
import React from "react"
import boxes from "./boxes"
import Box from "./Box"
export default function App() {
const [squares, setSquares] = React.useState(boxes)
const squareElements = squares.map(square => (
<Box key={square.id} on={square.on} />
))
return (

<main>
{squareElements}
</main>
)
}

Box.js
import React from "react"
export default function Box(props) {
const [on, setOn] = React.useState(props.on)
const styles = {
backgroundColor: on ? "#222222" : "transparent"
}
function toggle() {
setOn(prevOn => !prevOn)
}
return (

<div style={styles} className="box" onClick={toggle}></div>
)
}

CSS:
.box {
height: 100px;
width: 100px;
border: 1px solid black;
display: inline-block;
margin-right: 4px;
border-radius: 5px;
}

---

Derived State:
https://reactjs.org/blog/2018/06/07/you-probably-dont-need-derived-state.html

Boxes Change: we only use one state to do it
App.js
import React from "react"
import boxes from "./boxes"
import Box from "./Box"
export default function App() {
const [squares, setSquares] = React.useState(boxes)
function toggle(id) {
console.log(id) //important
}
const squareElements = squares.map(square => (
<Box
key={square.id}
id={square.id} //important
on={square.on}
toggle={toggle} //important
/>
))
return (

<main>
{squareElements}
</main>
)
}

Box.js
import React from "react"
export default function Box(props) {
const styles = {
backgroundColor: props.on ? "#222222" : "transparent"
}
return (

<div
style={styles}
className="box"
onClick={()=>props.toggle(props.id)} //important, only this way, we can pass parameter >
</div>
)
}

---

function toggle(id) {
setSquares((prevSquares) => {
return prevSquares.map((square) => {
return square.id === id ? { ...square, on: !square.on } : square;
});
});
}

---

{isShown && <p>{props.punchline}</p>} //true then show <p>, false then not

messages.length === 0 ?

<h1>You're all caught up!</h1> :
<h1>You have {messages.length} unread 
{messages.length > 1 ? "messages" : "message"}</h1>
-------------------------------------------------------------------------------------------------------------------------------
quiz:
1. What is "conditional rendering"?
When we want to only sometimes display something on the page
based on a condition of some sort

2. When would you use &&?
   When you want to either display something or NOT display it

3. When would you use a ternary?
   When you need to decide which thing among 2 options to display

4. What if you need to decide between > 2 options on
   what to display?
   Use an `if...else if... else` conditional or a `switch` statement

function App() {
let someVar
if () {
someVar = <SomeJSX />
} else if() {
...
} else {
...
}
return (

<div>{someVar}</div>
)
}

---

Forms:
Read first: https://reactjs.org/docs/forms.html

const [firstName, setFirstName] = React.useState("")
console.log(firstName)
function handleChange(event) {
setFirstName(event.target.value)
}
return (

<form>
<input
                type="text"
                placeholder="First Name"
                onChange={handleChange}
            />
</form>
)
}

---

Form:

export default function Form() {
const [firstName, setFirstName] = React.useState("")
const [lastName, setLastName] = React.useState("")
/\*\*
_ Challenge: Track the applicant's last name as well
_/

    console.log(firstName, lastName)

    function handleFirstNameChange(event) {
        setFirstName(event.target.value)
    }

    function handleLastNameChange(event) {
        setLastName(event.target.value)
    }
    return (
        <form>
            <input
                type="text"
                placeholder="First Name"
                onChange={handleFirstNameChange}
            />
            <input
                type="text"
                placeholder="Last Name"
                onChange={handleLastNameChange}
            />
        </form>
    )

## }

Terminal: find data
document.querySelector('input[name="developer-type"]:checked').value

1.  <input type="text" id="first-name" name="firstName" class="input" data-com.bitwarden.browser.user-edited="yes">
    document.getElementsByName('firstName')
    document.getElementsByName('firstName').forEach(text => {
        console.log(text.value);
    });

2.  <form method="POST" id="my-form"><label for="first-name">First Name: </label><input type="text" id="first-name" name="firstName" class="input" data-com.bitwarden.browser.user-edited="yes"><br><label for="last-name">Last Name: </label><input type="text" id="last-name" name="lastName" class="input" data-com.bitwarden.browser.user-edited="yes"><br><input type="submit" value="Submit"></form>
    document.getElementById('my-form') 
    document.getElementById('my-form').elements
    A=document.getElementById('my-form').elements
    console.log(A.firstName.value)
    console.log(A.lastName.value)

---

Form simplify:

const [Name, setName] = React.useState({ firstName: "", lastName: "" });
console.log(Name);
function handleChange(event) {
setName((preName) => {
return {
...preName,
[event.target.name]: event.target.value,
};
});
}

return (

<main>
<form method="POST" id="my-form">
<label for="first-name">First Name: </label>
<input
          type="text"
          id="first-name"
          name="firstName"
          class="input"
          onChange={handleChange}
        />
<br />
<label for="last-name">Last Name: </label>
<input
          type="text"
          id="last-name"
          name="lastName"
          class="input"
          onChange={handleChange}
        />
<br />
<input type="submit" value="Submit" />
</form>
<script src="index.pack.js"></script>
</main>
);
}

---

Form Controlled components:
https://reactjs.org/docs/forms.html#controlled-components

Checkbox:
<br />
<input type="checkbox" id="isFriendly" />
<label htmlFor="isFriendly">Are you friendly?</label>
<br />

import React from "react"

export default function Form() {
const [formData, setFormData] = React.useState(
{
firstName: "",
lastName: "",
email: "",
comments: "",
isFriendly: true
}
)

    function handleChange(event) {
        const {name, value, type, checked} = event.target
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [name]: type === "checkbox" ? checked : value      //important
            }
        })
    }

    return (
        <form>
            <input
                type="checkbox"
                id="isFriendly"
                checked={formData.isFriendly}
                onChange={handleChange}
                name="isFriendly"
            />
            <label htmlFor="isFriendly">Are you friendly?</label>
            <br />
        </form>
    )

}

---

Radio Button:
import React from "react"

export default function Form() {
const [formData, setFormData] = React.useState(
{
firstName: "",
lastName: "",
email: "",
comments: "",
isFriendly: true,
employment: ""
}
)
console.log(formData.employment)

    function handleChange(event) {
        const {name, value, type, checked} = event.target
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [name]: type === "checkbox" ? checked : value
            }
        })
    }

    return (
        <form>
            <fieldset>
                <legend>Current employment status</legend>

                <input
                    type="radio"
                    id="unemployed"
                    name="employment"
                    value="unemployed"
                    checked={formData.employment === "unemployed"}
                    onChange={handleChange}
                />
                <label htmlFor="unemployed">Unemployed</label>
                <br />

                <input
                    type="radio"
                    id="part-time"
                    name="employment"
                    value="part-time"
                    checked={formData.employment === "part-time"}
                    onChange={handleChange}
                />
                <label htmlFor="part-time">Part-time</label>
                <br />

                <input
                    type="radio"
                    id="full-time"
                    name="employment"
                    value="full-time"
                    checked={formData.employment === "full-time"}
                    onChange={handleChange}
                />
                <label htmlFor="full-time">Full-time</label>
                <br />

            </fieldset>
        </form>
    )

}

---

Select & Option:
import React from "react"

export default function Form() {
const [formData, setFormData] = React.useState(
{
firstName: "",
lastName: "",
email: "",
comments: "",
isFriendly: true,
employment: "",
favColor: ""
}
)
console.log(formData.favColor)

    function handleChange(event) {
        console.log(event)
        const {name, value, type, checked} = event.target
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [name]: type === "checkbox" ? checked : value
            }
        })
    }

    return (
        <form>
            <label htmlFor="favColor">What is your favorite color?</label>
            <br />
            <select
                id="favColor"
                value={formData.favColor}
                onChange={handleChange}
                name="favColor"
            >
                <option value="">-- Choose --</option>
                <option value="red">Red</option>
                <option value="orange">Orange</option>
                <option value="yellow">Yellow</option>
                <option value="green">Green</option>
                <option value="blue">Blue</option>
                <option value="indigo">Indigo</option>
                <option value="violet">Violet</option>
            </select>
        </form>
    )

}

---

Button:

<button>Submit</button> or
<input type="submit" value="Submit" />

---

submit the form:

import React from "react"

export default function Form() {
const [formData, setFormData] = React.useState(
{
firstName: "",
lastName: "",
email: "",
comments: "",
isFriendly: true,
employment: "",
favColor: ""
}
)

    function handleChange(event) {
        const {name, value, type, checked} = event.target           //{} is important
        setFormData(prevFormData => {
            return {
                ...prevFormData,
                [name]: type === "checkbox" ? checked : value
            }
        })
    }

    function handleSubmit(event) {
        event.preventDefault()       //important: prevent default render
        // submitToApi(formData)
        console.log(formData)
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="First Name"
                onChange={handleChange}
                name="firstName"
                value={formData.firstName}
            />
            <input
                type="text"
                placeholder="Last Name"
                onChange={handleChange}
                name="lastName"
                value={formData.lastName}
            />
            <input
                type="email"
                placeholder="Email"
                onChange={handleChange}
                name="email"
                value={formData.email}
            />
            <textarea
                value={formData.comments}
                placeholder="Comments"
                onChange={handleChange}
                name="comments"
            />
            <input
                type="checkbox"
                id="isFriendly"
                checked={formData.isFriendly}
                onChange={handleChange}
                name="isFriendly"
            />
            <label htmlFor="isFriendly">Are you friendly?</label>
            <br />
            <br />

            <fieldset>
                <legend>Current employment status</legend>
                <input
                    type="radio"
                    id="unemployed"
                    name="employment"
                    value="unemployed"
                    checked={formData.employment === "unemployed"}
                    onChange={handleChange}
                />
                <label htmlFor="unemployed">Unemployed</label>
                <br />

                <input
                    type="radio"
                    id="part-time"
                    name="employment"
                    value="part-time"
                    checked={formData.employment === "part-time"}
                    onChange={handleChange}
                />
                <label htmlFor="part-time">Part-time</label>
                <br />

                <input
                    type="radio"
                    id="full-time"
                    name="employment"
                    value="full-time"
                    checked={formData.employment === "full-time"}
                    onChange={handleChange}
                />
                <label htmlFor="full-time">Full-time</label>
                <br />
            </fieldset>
            <br />

            <label htmlFor="favColor">What is your favorite color?</label>
            <br />
            <select
                id="favColor"
                value={formData.favColor}
                onChange={handleChange}
                name="favColor"
            >
                <option value="red">Red</option>
                <option value="orange">Orange</option>
                <option value="yellow">Yellow</option>
                <option value="green">Green</option>
                <option value="blue">Blue</option>
                <option value="indigo">Indigo</option>
                <option value="violet">Violet</option>
            </select>
            <br />
            <br />
            <button>Submit</button>
        </form>
    )

}

---

Quize:

1. In a vanilla JS app, at what point in the form submission
   process do you gather all the data from the filled-out form?
   Right before the form is submitted.

2. In a React app, when do you gather all the data from
   the filled-out form?
   As the form is being filled out. The data is all held in local state.

3. Which attribute in the form elements (value, name, onChange, etc.)
   should match the property name being held in state for that input?
   `name` property.

4. What's different about saving the data from a checkbox element
   vs. other form elements?
   A checkbox uses the `checked` property to determine what should
   be saved in state. Other form elements use the `value` property instead.

5. How do you watch for a form submit? How can you trigger
   a form submit?

- Can watch for the submit with an onSubmit handler on the `form` element.
- Can trigger the form submit with a button click.

---

submit form practice:

import React from "react"

export default function App() {
const [formData, setFormData] = React.useState({
email: "",
password: "",
passwordConfirm: "",
joinedNewsletter: true
})

    /**
     * Challenge: Connect the form to local state
     *
     * 1. Create a state object to store the 4 values we need to save.
     * 2. Create a single handleChange function that can
     *    manage the state of all the inputs and set it up
     *    correctly
     * 3. When the user clicks "Sign up", check if the
     *    password & confirmation match each other. If
     *    so, log "Successfully signed up" to the console.
     *    If not, log "passwords do not match" to the console.
     * 4. Also when submitting the form, if the person checked
     *    the "newsletter" checkbox, log "Thanks for signing
     *    up for our newsletter!" to the console.
     */

    function handleChange(event) {
        const {name, value, type, checked} = event.target
        setFormData(prevFormData => ({
            ...prevFormData,
            [name]: type === "checkbox" ? checked : value
        }))
    }

    function handleSubmit(event) {
        event.preventDefault()
        if(formData.password === formData.passwordConfirm) {
            console.log("Successfully signed up")
        } else {
            console.log("Passwords do not match")
            return                                                // important, I am easy to miss this part
        }

        if(formData.joinedNewsletter) {
            console.log("Thanks for signing up for our newsletter!")
        }
    }

    return (
        <div className="form-container">
            <form className="form" onSubmit={handleSubmit}>
                <input
                    type="email"
                    placeholder="Email address"
                    className="form--input"
                    name="email"
                    onChange={handleChange}
                    value={formData.email}
                />
                <input
                    type="password"
                    placeholder="Password"
                    className="form--input"
                    name="password"
                    onChange={handleChange}
                    value={formData.password}
                />
                <input
                    type="password"
                    placeholder="Confirm password"
                    className="form--input"
                    name="passwordConfirm"
                    onChange={handleChange}
                    value={formData.passwordConfirm}
                />

                <div className="form--marketing">
                    <input
                        id="okayToEmail"
                        type="checkbox"
                        name="joinedNewsletter"
                        onChange={handleChange}
                        checked={formData.joinedNewsletter}
                    />
                    <label htmlFor="okayToEmail">I want to join the newsletter</label>
                </div>
                <button
                    className="form--submit"
                >
                    Sign up
                </button>
            </form>
        </div>
    )

}

---

Making Api calls: fetch get data

import React from "react"

export default function App() {
const [starWarsData, setStarWarsData] = React.useState({})

    console.log("Component rendered")

    fetch("https://swapi.dev/api/people/1")
        .then(res => res.json())
        .then(data => console.log(data))

    // side effects

    return (
        <div>
            <pre>{JSON.stringify(starWarsData, null, 2)}</pre>
        </div>
    )

## }

This is a wrong example: it will loop render, it is bad

import React from "react"

export default function App() {
const [starWarsData, setStarWarsData] = React.useState({})

    console.log("Component rendered")

    fetch("https://swapi.dev/api/people/1")
        .then(res => res.json())
        .then(data => setStarWarsData(data))          //setStarWarsData(data)  here it is bad, it will cause page rerender every seconds

    // side effects

    return (
        <div>
            <pre>{JSON.stringify(starWarsData, null, 2)}</pre>
        </div>
    )

## }

useEffect to deal with side Effects:
https://reactjs.org/docs/hooks-effect.html
Deeper：https://overreacted.io/a-complete-guide-to-useeffect/

import React from "react"
export default function App() {
const [starWarsData, setStarWarsData] = React.useState({})
const [count, setCount] = React.useState(0)

    console.log("Component rendered")

    React.useEffect(() => {
        console.log("Effect function ran")
    }, [count])                     // when count change, useEffect will run

    return (
        <div>
            <pre>{JSON.stringify(starWarsData, null, 2)}</pre>
            <h2>The count is {count}</h2>
            <button onClick={() => setCount(prevCount => prevCount + 1)}>Add</button>
        </div>
    )

## }

quiz:

1. What is a "side effect" in React? What are some examples?

- Any code that affects an outside system.
- local storage, API, websockets, two states to keep in sync

2. What is NOT a "side effect" in React? Examples?

- Anything that React is in charge of.
- Maintaining state, keeping the UI in sync with the data,
  render DOM elements

3. When does React run your useEffect function? When does it NOT run
   the effect function?

- As soon as the component loads (first render)
- On every re-render of the component (assuming no dependencies array)
- Will NOT run the effect when the values of the dependencies in the
  array stay the same between renders

4. How would you explain what the "dependecies array" is?

- Second paramter to the useEffect function
- A way for React to know whether it should re-run the effect function

---

import React from "react"

export default function App() {
const [starWarsData, setStarWarsData] = React.useState({})
const [count, setCount] = React.useState(0)

    /**
     * Quiz:
     * 1. What will happen if I put back our Star Wars API call
     *    into the effect function?
     * 2. How will the useEffect be different if I use
     *    setStarWarsData() instead of console.log()
     * 3. What SHOULD be in our dependencies array in this case?
     */
    React.useEffect(function() {
        console.log("Effect ran")
        fetch("https://swapi.dev/api/people/1")
            .then(res => res.json())
            .then(data => setStarWarsData(data))
    }, [])                                            //important: only run once, this value of dependencies array must appear at above function

    return (
        <div>
            <pre>{JSON.stringify(starWarsData, null, 2)}</pre>
            <h2>The count is {count}</h2>
            <button onClick={() => setCount(prevCount => prevCount + 1)}>Add</button>
        </div>
    )

}

---

import React from "react"

export default function App() {
const [starWarsData, setStarWarsData] = React.useState({})
const [count, setCount] = React.useState(1)

    /**
     * Challenge: Combine `count` with the request URL
     * so pressing the "Get Next Character" button will
     * get a new character from the Star Wars API.
     * Remember: don't forget to consider the dependencies
     * array!
     */

    React.useEffect(function() {
        console.log("Effect ran")
        fetch(`https://swapi.dev/api/people/${count}`)    or fetch("https://swapi.dev/api/people/" + count)  //important
            .then(res => res.json())
            .then(data => setStarWarsData(data))
    }, [count])

    return (
        <div>
            <h2>The count is {count}</h2>
            <button onClick={() => setCount(prevCount => prevCount + 1)}>Get Next Character</button>
            <pre>{JSON.stringify(starWarsData, null, 2)}</pre>
        </div>
    )

}

---

Meme useEffect:
import React from "react"

export default function Meme() {
const [meme, setMeme] = React.useState({
topText: "",
bottomText: "",
randomImage: "http://i.imgflip.com/1bij.jpg"
})
const [allMemes, setAllMemes] = React.useState([])

    React.useEffect(() => {
        fetch("https://api.imgflip.com/get_memes")
            .then(res => res.json())
            .then(data => setAllMemes(data.data.memes))               //important
    }, [])

    function getMemeImage() {
        const randomNumber = Math.floor(Math.random() * allMemes.length)
        const url = allMemes[randomNumber].url
        setMeme(prevMeme => ({
            ...prevMeme,
            randomImage: url
        }))

    }

    function handleChange(event) {
        const {name, value} = event.target
        setMeme(prevMeme => ({
            ...prevMeme,
            [name]: value
        }))
    }

    return (
        <main>
            <div className="form">
                <input
                    type="text"
                    placeholder="Top text"
                    className="form--input"
                    name="topText"
                    value={meme.topText}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    placeholder="Bottom text"
                    className="form--input"
                    name="bottomText"
                    value={meme.bottomText}
                    onChange={handleChange}
                />
                <button
                    className="form--button"
                    onClick={getMemeImage}
                >
                    Get a new meme image 🖼
                </button>
            </div>
            <div className="meme">
                <img src={meme.randomImage} className="meme--image" />
                <h2 className="meme--text top">{meme.topText}</h2>
                <h2 className="meme--text bottom">{meme.bottomText}</h2>
            </div>
        </main>
    )

## }

import React from "react"
import WindowTracker from "./WindowTracker"

export default function App() {
/\*\*
_ Challenge:
_ 1. Create state called `show`, default to `true`
_ 2. When the button is clicked, toggle `show`
_ 3. Only display `<WindowTracker>` if `show` is `true`
\*/

    const [show, setShow] = React.useState(true)

    function toggle() {
        setShow(prevShow => !prevShow)
    }

    return (
        <div className="container">
            <button onClick={toggle}>
                Toggle WindowTracker
            </button>
            {show && <WindowTracker />}
        </div>
    )

}

---

WindowTracker.js:

import React from "react"
export default function WindowTracker() {
const [windowWidth, setWindowWidth] = React.useState(window.innerWidth)
React.useEffect(() => {
window.addEventListener("resize", function() {
setWindowWidth(window.innerWidth)
})
}, [])
return (

<h1>Window width: {windowWidth}</h1>
)
}

App.js:

import React from "react"
import WindowTracker from "./WindowTracker"
export default function App() {
/\*\*
_ Challenge:
_ 1. Create state called `show`, default to `true`
_ 2. When the button is clicked, toggle `show`
_ 3. Only display `<WindowTracker>` if `show` is `true`
\*/
const [show, setShow] = React.useState(true)
function toggle() {
setShow(prevShow => !prevShow)
}
return (

<div className="container">
<button onClick={toggle}>
Toggle WindowTracker
</button>
{show && <WindowTracker />} // important: this will lead memory leak, because even we don't display windowtracker, we still listen to resize
</div>
)
}

---

useEffect: Add clear up:

import React from "react"
export default function WindowTracker() {  
 const [windowWidth, setWindowWidth] = React.useState(window.innerWidth)
React.useEffect(() => {
function watchWidth() {
console.log("Setting up...")
setWindowWidth(window.innerWidth)
}
window.addEventListener("resize", watchWidth)
return function() {
console.log("Cleaning up...")
window.removeEventListener("resize", watchWidth)
}
}, [])

    return (
        <h1>Window width: {windowWidth}</h1>
    )

}

---

useEffect async:
/\*_
useEffect takes a function as its parameter. If that function
returns something, it needs to be a cleanup function. Otherwise,
it should return nothing. If we make it an async function, it
automatically retuns a promise instead of a function or nothing.
Therefore, if you want to use async operations inside of useEffect,
you need to define the function separately inside of the callback
function, as seen below:
_/

    React.useEffect(() => {
        async function getMemes() {
            const res = await fetch("https://api.imgflip.com/get_memes")
            const data = await res.json()
            setAllMemes(data.data.memes)
        }
        getMemes()
    }, [])

---

axios:

componentDidMount(){
axios.get('http://localhost:4200/serverport')
.then(response => {
this.setState({ serverports: response.data });
})
.catch(function (error) {
console.log(error);
})
}

---

const axios = require("axios");
const sendGetRequest = async () => {
try {
const resp = await axios
.get("http://localhost:4000/users")
.then((res) => {
setState((prev) => {
return { ...prev, usersCollection: res.data };
});
});
} catch (err) {
// Handle Error Here
console.error(err);
}
};
sendGetRequest();

---

react-mde
react-mde doesn't apply css
import "react-mde/lib/styles/css/react-mde-all.css";

localstorage:
https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage

const [notes, setNotes] = React.useState(
JSON.parse(localStorage.getItem("notes")) || []); //get items

React.useEffect(() => {
localStorage.setItem("notes", JSON.stringify(notes)); //add items
}, [notes]);

const [state, setState] = React.useState(console.log("State initialization")) //important, will rerun this code when changes

const [state, setState] = React.useState(
function() { //important,will not rerun this code when changesm it is lazy state initialization
return console.log("State initialization")  
 }
)

like:
const [notes, setNotes] = React.useState(
JSON.parse(localStorage.getItem("notes")) || []; //rerun every time
});

const [notes, setNotes] = React.useState(() => {
return JSON.parse(localStorage.getItem("notes")) || []; //only run once initialization
});

Storage data2:

meme.js
export default {
success: true,
data: {
memes: [
{
id: "181913649",
name: "Drake Hotline Bling",
url: "https://i.imgflip.com/30b1gx.jpg",
width: 1200,
height: 1200,
box_count: 2,
},
{
id: "87743020",
name: "Two Buttons",
url: "https://i.imgflip.com/1g8my4.jpg",
width: 600,
height: 908,
box_count: 3,
}
},
],
},
};

split:
{note.body.split("\n")[0].replace("# ", "")}

---

move modified notes to the top of the lists:
rearrange the note:

function updateNote(text) {
//rearrange the arry
setNotes((oldNotes) => {
var newarray = [];
for (let i = 0; i < oldNotes.length; i++) {
const oldNote = oldNotes[i];
oldNote.id === currentNoteId
? newarray.unshift({ ...oldNote, body: text })
: newarray.push(oldNote);
}
console.log(notes);
return newarray;
});

---

add event to react:
onClick={(event) => props.deleteNote(event, note.id)} //important, call back function

setNotes(oldNotes => oldNotes.filter(note => note.id !== noteId)) // important: filer, only return true value in array

random generate number from 1-9:
Math.ceil(Math.random() \* 9); //ceil means start from 1, include 1

---

every():
const allHeld = dice.every(die => die.isHeld) //if one is false, return false; only if all true then return true
const firstValue = dice[0].value
const allSameValue = dice.every(die => die.value === firstValue)
if (allHeld && allSameValue) {
setTenzies(true)
console.log("You won!")
}

---

https://github.com/alampros/react-confetti#readme
congradulation effect:

---

const questionElements =
state &&
state.map((question, i) => {
return (

<div key={i}> //important, how to find id
<Singlequiz
            name={question.question}
            A={question.correct_answer}
            B={question.incorrect_answers[0]}
            C={question.incorrect_answers[1]}
            D={question.incorrect_answers[2]}
          />
</div>
);
});

---

Final program: quizz

useRef

1. focus, when click button, cursor auto focus on input box
   function Component() {
   const inputRef = useRef(null)
   const focusInput = () => {
   inputRef.current.focus()
   }
   return (
   <>
   <input ref={inputRef} />
   <button onClick={focusInput}>Focus Input</button>
   </>
   )
   }

2. save previouse date
   function Component() {
   const [name, setName] = useState('Kyle')
   const previousName = useRef(null)
   useEffect(() => {
   previousName.current = name
   }, [name])
   return (
   <>
   <input value={name} onChange={e => setName(e.target.value)} />
   <div>{previousName.current} => {name}</div>
   </>
   )
   }

3. count number
   function State() {
   const [rerenderCount, setRerenderCount] = useState(0);
   useEffect(() => {
   setRerenderCount(prevCount => prevCount + 1);
   });
   return <div>{rerenderCount}</div>;
   }

4. parent call child function
   parent.js:
   const childRef = React.useRef(null);
   const handleClick = () => {
   setFlag(true);
   childRef.current.handleSubmit();
   };
   return (
   <div key={i}>
   <button onClick={handleClick}>Check Answers</button>
   <Singlequiz ref={childRef} />
   </div>
   );

child.js:
const Singlequiz = React.forwardRef((props, ref) => {
React.useImperativeHandle(ref, () => ({
handleSubmit() {
console.log("handleSubmit1");
},
}));
return (

<div>
...
</div>
);
});
export default Singlequiz;

---

import { nanoid } from "nanoid";
id: nanoid(),

import arrayShuffle from "array-shuffle";
arrayShuffle([1,2,3]])

---

Hooks:

Both useState and useMemo will remember a value across renders. The difference is that:
useMemo does not cause a re-render, while useState does
useMemo only runs when its dependencies (if any) have changed,
while setSomeState (second array item returned by useState) does not have such a dependency array
Both useMemo and useEffect only runs when their dependencies change (if any). The difference is that:
useEffect runs after a render happens,
while useMemo runs before

---

---

---

---

## 分界线

npx create-react-app@latest {project name}
cd {project name}
npm i styled-components
npm install axios
npm start
git add .
git commit -m 'your message'
git push
git push origin master

---

styled-components:
src/components/styles/Container.styled.js
src/components/styles/Input.styled.js
import styled from "styled-components";
export const Input = styled.input`  width: 20px
  background:green`;

App.js:
import { Container } from "./components/styles/Container.styled";
import { Input } from "./components/styles/Input.styled";

function App() {
return (

<div>
<Container>
<h1>Hello World</h1>
</Container>
<Input placeholder="input" />
</div>
);
}
export default App;

---

LifeCycle:
componentDidMount()：after all html finished, then start run
componentWillMount(): before run(first run)

import React, { Component } from 'react';
class App extends Component {
constructor(props){ // step 2
super(props);
this.state = {
data: 'Jordan Belfort'
}
}
componentWillMount(){ // step 1
console.log('First this called');
}

getData(){ // step 5
setTimeout(() => {
console.log('Our data is fetched');
this.setState({
data: 'Hello WallStreet'
})
}, 1000)
}

componentDidMount(){ // step 4
this.getData();
}

render() { // step 3
return(

<div>
{this.state.data}
</div>
)
}
}

## export default App;

json-server:
npm install -g json-server

creat db.json:
{ "people": [{ "id": 0, "name": "Eva" }] }

run:
json-server db.json
then we get a server start, when we operate date by rest-client, data will not save
but if we input "s", will create a snapshot db-1657394053801.json with all data
control c : close server

run
json-server -h
to find help, like how to change port

---

rest-client: like postman, but can use in visual studio code
have different environment, like guileon, test...
https://www.youtube.com/watch?v=8uyTn4cg8Xc

GET http://localhost:3000/people //Get data
GET http://localhost:3000/people?q=Randy //Get data query "Randy" include

POST http://localhost:3000/people HTTP/1.1 //Add data
content-type: application/json
{
"id": "3",
"name": "john3"

}

PUT http://localhost:3000/people/3 HTTP/1.1 //Change data
content-type: application/json
//important: have to have this empty line
{
"name": "john3change"
}

---

npm install faker lodash

faker: is a JavaScript library that generates fake data for you. Whether
you need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you

lodash:Lodash makes JavaScript easier by taking the hassle out of working with arrays, numbers, objects, strings, etc.
Lodash’s modular methods are great for:
Iterating arrays, objects, & strings
Manipulating & testing values
Creating composite functions

lodash.times(100) performs a 100th time loop with n as the counter.

create generate.js:
module.exports = function () {
var faker = require("faker");
var _ = require("lodash");
return {
people: _.times(100, function (n) {
return {
id: n,
name: faker.name.findName(),
avatar: faker.internet.avatar(),
};
}),
};
};

run:
json-server generate.js

use RestClient get data:
GET http://localhost:3000/people  
GET http://localhost:3000/people?q=Randy

---

list [] 才能用 map display data

<button type="submit" onClick={() => window.location.reload(false)}> //important: click button refresh the page
Add
</button>

---

---

---

---

---

Another Class:
Layout Component:

---

brew install node@14
Node -v

Npm init
Npm install express mongoose --save

npx create-react-app DynamicChart --template typescript
npm install @amcharts/amcharts5

import _ as am5 from "@amcharts/amcharts5";
import _ as am5xy from "@amcharts/amcharts5/xy";

---

npx create-next-app app name
npx create-next-app --ts app name //typesript

---

Alt+command+F align code
npm i element-react --legacy-peer-deps
npm install element-theme-default --legacy-peer-deps

npm view react version

---

React-native:

npm install react-native-elements --legacy-peer-deps

---

element library: A Desktop UI Library
Element, a Vue 2.0 based component library for developers, designers and product managers

## Start program

```
npx create-react-app@latest {project name}
cd {project name}
npm i styled-components
npm install axios
npm i router
npm start
git add .
git commit -m 'your message'
git push
git push origin master
```

## Test

### Skills

1. When test web inpute, I recommend using static data initially, then using random data (or fuzzing-techniques) once the tests are working & stable to try to find the edge-case bugs.

## MERN app example

https://www.positronx.io/react-axios-tutorial-make-http-get-post-requests/

1. Mongoose is an Object Data Modeling (ODM) library for MongoDB and Node.js.

```
npm install bootstrap --save
npm install react-router-dom --save

sudo npm install -g --force nodemon
# then run "nodemon server", it will work

```

How to start program

```
/mern_axios_example
npm start

/mern_axios_example/server
nodemon server
```

### Mongodb atabase

```
mongosh
show dbs
use mydatabase
show collections
db.users.find()

#delete all documents
db.users.deleteMany({})
```

### Webpack

```
npm init -y    // -y means skip all questions
npm i -D webpack webpack-cli   //-D means development dependencies

package.json
"script":{
    "build":"webpack --mode production"
}

npm run build

npm i uuid
//change part of code
npm run build
npm remove uuid
//change part of code
npm run build

/create and edit webpack.config.js
npm run build

npm i -D sass style-loader css-loader sass-loader
npm i -D html-webpack-plugin

.container
<div class="container"></div>
#joke.joke
<div id="joke" class="joke"></div>
button#jokeBtn.btn
<button id="jokeBtn" class="btn"></button>


```

---

### Typescript

npx create-react-app my-app --template typescript
cd {project name}
npm i styled-components
npm install axios --save
npm install @amcharts/amcharts5
npm i router
npm start
git add .
git commit -m 'your message'
git push
git push origin master

npm install axios --save
src/components/List.tsxls

---

## npm install @mui/material @emotion/react @emotion/styled

nvm:
install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

nvm install 16.16.0
nvm ls
nvm use 16
nvm uninstall 16.16.0

source ~/.nvm/nvm.sh

---

XML:XML is a software- and hardware-independent tool for storing and transporting data.
XML stands for eXtensible Markup Language
XML was designed to store and transport data, machine and people can understand it.

JSX:JSX is an extension to javascript. (need babel to do it work)JSX stands for JavaScript XML. JSX allows us to write HTML in React. JSX makes it easier to write and add HTML in React.

.ts is used for plain Typescript files and do not support adding JSX Elements
.tsx for files which contain JSX. better than .ts

On another point of view, you can copy everything from a .ts file and paste on .tsx file, and you don't need to modify anything. But if you're copying from a .tsx file you need to refactor it by removing the JSX elements.

Hint: If you use <> to do type-casting in your .ts file and you paste that into a .tsx file, then that will lead to errors.

Babel.js:transpile javascript code and rewrite to something else, then other(older or new) browers can render; it is invisible and run backend
