var navbar = `
<nav class="navbar navbar-default">
	<div class="container-fluid">
		<ul class="nav navbar-nav">
			<li id="index"><a href="./index.html">Home</a></li>
			<li id="keralaCubers"><a href="./keralaCubers.html">Kerala Cubers</a></li>
			<li id="rankings"><a href="./rankings.html">Rankings</a></li>
			<li id="competitions"><a href="./competitions.html">Competitions</a></li>
			<li id="contactUs"><a href="./contactUs.html">Contact Us</a></li>
		</ul>
	</div>
</nav>
`;
document.getElementById("nav").innerHTML = navbar;
document.getElementById(window.location.href.match("[^/]*(?=\\.html)")).classList.add("active");