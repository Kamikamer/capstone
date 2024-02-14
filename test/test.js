// Ignore this
/**
 * IGNOREEE
 */

document.getElementsByName('provider')[0].addEventListener('change', swapProvider);

function swapProvider() {
  const currentSearchEngine = document.getElementsByName("provider")[0].value;

  console.log(`Current engine:  ${currentSearchEngine}`);
  if(currentSearchEngine === "bing") {
    document.getElementsByClassName('homesearch')[0].placeholder="Why are you using bing..? Anyway, search here!";
  }

  if(currentSearchEngine === "ddg") {
    document.getElementsByClassName('homesearch')[0].placeholder="DuckDuckGoos- Nop it's duckduckgo here!";
  }

  if(currentSearchEngine === "google") {
    document.getElementsByClassName('homesearch')[0].placeholder="Google here!";
  }

  if(currentSearchEngine === "startpage") {
    document.getElementsByClassName('homesearch')[0].placeholder="Fancy a private search engine? Search here!";
  }

  if(currentSearchEngine === "tiles") {
    document.getElementsByClassName('homesearch')[0].placeholder="Choose the tile you want! E.g. Proxmox";
  }

  if (currentSearchEngine === "baidu") {
    document.getElementsByClassName('homesearch')[0].placeholder="在这便！";
  }
}

swapProvider();

function backButtonLogic() {
  const allLinks = document.getElementsByClassName("link");
  Array.from(allLinks).forEach(element => {
    if (element.getAttribute("href") === "https://heimdall.kami.wtf") {
      element.target = "_self";
      element.classList.add("backButton");
      if (document.URL == "https://heimdall.kami.wtf" || document.URL == "https://heimdall.kami.wtf/" || document.URL == "https://heimdall.kami.boo" || document.URL == "https://heimdall.kami.boo/") {
        console.log("Hiding back button")
        element.parentElement.parentElement.setAttribute("style", "display: none;");
      }
    }
  });
}

window.addEventListener('load', () => {
  backButtonLogic();
});