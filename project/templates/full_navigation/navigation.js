import { gsap } from "gsap/dist/gsap";
    
import { SplitText } from "gsap/dist/SplitText";
import { CustomEase } from "gsap/dist/CustomEase";

gsap.registerPlugin(SplitText, CustomEase);
CustomEase.create("hop", "0.85, 0, 0.15, 1");

const menu = document.querySelector("menu");
const menuToogle = document.querySelector(".nav-toggle-btn");
let isMenuOpen = false;

SplitText.create(".menu a, .menu p", {
    type: "lines",
    mask: "lines",
    linesClass: "line",
});