(function() {
    var tap;
  
    tap = "click";
  
    if (Modernizr.touch) {
      tap = "touchstart";
    }
  
    $(document).on(tap, '.brick.closed', function(event) {
      var $this;
      $this = $(this);
      $this.animate({
        'width': '100%'
      }, 'fast', function() {});
      $this.removeClass('closed');
      return $this.addClass('open');
    });
  
    $(document).on(tap, '.brick a.js-close', function(event) {
      var $brick;
      $brick = $(this).closest('.brick');
      return $brick.animate({
        'width': '120px'
      }, 'fast', function() {
        $brick.removeClass('open');
        return $brick.addClass('closed');
      });
    });
  
  }).call(this);
  
  //# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiPGFub255bW91cz4iXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7QUFBQSxNQUFBOztFQUFBLEdBQUEsR0FBTTs7RUFDTixJQUFxQixTQUFTLENBQUMsS0FBL0I7SUFBQSxHQUFBLEdBQUssYUFBTDs7O0VBRUEsQ0FBQSxDQUFFLFFBQUYsQ0FBVyxDQUFDLEVBQVosQ0FBZSxHQUFmLEVBQW9CLGVBQXBCLEVBQXFDLFFBQUEsQ0FBQyxLQUFELENBQUE7QUFDbkMsUUFBQTtJQUFBLEtBQUEsR0FBUSxDQUFBLENBQUUsSUFBRjtJQUNSLEtBQUssQ0FBQyxPQUFOLENBQWM7TUFBRSxPQUFBLEVBQVM7SUFBWCxDQUFkLEVBQW1DLE1BQW5DLEVBQTJDLFFBQUEsQ0FBQSxDQUFBLEVBQUEsQ0FBM0M7SUFDQSxLQUFLLENBQUMsV0FBTixDQUFrQixRQUFsQjtXQUNBLEtBQUssQ0FBQyxRQUFOLENBQWUsTUFBZjtFQUptQyxDQUFyQzs7RUFNQSxDQUFBLENBQUUsUUFBRixDQUFXLENBQUMsRUFBWixDQUFlLEdBQWYsRUFBb0IsbUJBQXBCLEVBQXlDLFFBQUEsQ0FBQyxLQUFELENBQUE7QUFDdkMsUUFBQTtJQUFBLE1BQUEsR0FBUyxDQUFBLENBQUUsSUFBRixDQUFPLENBQUMsT0FBUixDQUFnQixRQUFoQjtXQUNULE1BQU0sQ0FBQyxPQUFQLENBQWU7TUFBRSxPQUFBLEVBQVM7SUFBWCxDQUFmLEVBQXFDLE1BQXJDLEVBQTZDLFFBQUEsQ0FBQSxDQUFBO01BQzNDLE1BQU0sQ0FBQyxXQUFQLENBQW1CLE1BQW5CO2FBQ0EsTUFBTSxDQUFDLFFBQVAsQ0FBZ0IsUUFBaEI7SUFGMkMsQ0FBN0M7RUFGdUMsQ0FBekM7QUFUQSIsInNvdXJjZXNDb250ZW50IjpbInRhcCA9IFwiY2xpY2tcIlxudGFwID1cInRvdWNoc3RhcnRcIiBpZiBNb2Rlcm5penIudG91Y2hcblxuJChkb2N1bWVudCkub24gdGFwLCAnLmJyaWNrLmNsb3NlZCcsIChldmVudCkgLT5cbiAgJHRoaXMgPSAkKHRoaXMpXG4gICR0aGlzLmFuaW1hdGUgeyAnd2lkdGgnOiAnMTAwJScgfSwgJ2Zhc3QnLCAoKSAtPlxuICAkdGhpcy5yZW1vdmVDbGFzcygnY2xvc2VkJylcbiAgJHRoaXMuYWRkQ2xhc3MoJ29wZW4nKVxuXG4kKGRvY3VtZW50KS5vbiB0YXAsICcuYnJpY2sgYS5qcy1jbG9zZScsIChldmVudCkgLT5cbiAgJGJyaWNrID0gJCh0aGlzKS5jbG9zZXN0KCcuYnJpY2snKVxuICAkYnJpY2suYW5pbWF0ZSB7ICd3aWR0aCc6ICcxMjBweCcgfSwgJ2Zhc3QnLCAoKSAtPlxuICAgICRicmljay5yZW1vdmVDbGFzcygnb3BlbicpXG4gICAgJGJyaWNrLmFkZENsYXNzKCdjbG9zZWQnKVxuIl19
  //# sourceURL=coffeescript







  /* header */
html {
    box-sizing: border-box;
  }
  
  *, *:before, *:after {
    box-sizing: inherit;
  }
  
  html{
    height: 100%;
    padding: 16px;
    background-color: #252326;
    background-image: url('http://christiannaths.com/code/admin-interface/dots.png'), url('http://christiannaths.com/code/admin-interface/route-66.jpg');
    background-position: center center, center, center;
    background-attachment: fixed, fixed;
    background-size: auto, cover;
  }
  
  body{
    height: 100%;
    margin: 0;
    font: 16px/24px normal "Open Sans", trebuchet, sans-serif;
    font-weight: 100;
    color: #616161;
    color: #252326;
  }
  
  h1, h2, h3, h4, h5{
    margin-top: 0;
    font-family: inherit;
    font-weight: inherit;
    font-size: 21px;
  }
  
  a{
    text-decoration: none;
    color: #fff;
  }
  
  .brick{
    display: inline-block;
    width: 100%;
    padding: 16px;
    margin-bottom: 8px;
    margin-right: 8px;
    background-color: #e7e7e7;
    vertical-align: top;
  }
  
  .icon{
    display: inline-block;
    float: right;
    width: 30px;
    height: 30px;
    font-size: 1.5em;
    font-weight: 100;
    color: rgba(255, 255, 255, 0.75);
    line-height: 1.5;
    text-align: center;
  
  }
  
  header > hgroup{
    margin-bottom: 32px;
    color: #fff;
  }
  
  header h1{
    margin-bottom: 0;
    font-size: 28px;
  }
  
  header a{
    color: #a93447;
  }
  
  nav{
    margin-bottom: 32px;
  }
  
  nav ul{
    margin: 0;
    padding: 0;
    list-style: none;
  }
  
  nav ul li{
    display: inline;
  }
  
  nav ul li a.brick{
    position: relative;
    font-family: inherit;
    font-weight: inherit;
    color: #616161;
    color: #252326;
    line-height: 2;
    background-color: #252326;
    background-color: #F3F3F3;
    background-color: #e7e7e7;
    border-left: 3px solid #616161
  }
  
  nav ul li a.brick .icon{
    position: absolute;
    right: 0;
    top: 0;
    height: 64px;
    width: 64px;
    font-size: 2em;
    color: #fff;
    line-height: 2.25;
    background: #616161;
  }
  
  nav ul li a.dashboard{
    border-color: #B93861;
  }
  
  nav ul li a.dashboard .icon{
    background-color: #B93861;
  }
  
  nav ul li a.pages{
    border-color: #34ABD7;
  }
  
  nav ul li a.pages .icon{
    background-color: #34ABD7;
  }
  
  nav ul li a.navigation{
    border-color: #158A53;
  }
  
  nav ul li a.navigation .icon{
    background-color: #158A53;
  }
  
  nav ul li a.users{
    border-color: #D95235;
  }
  
  nav ul li a.users .icon{
    background-color: #D95235;
  }
  
  nav ul li a.settings{
    /*border-color: #34ABD7;*/
  }
  
  nav ul li a.settings .icon{
    /*background-color: #34ABD7;*/
  }
  
  #content > header{
    position: relative;
    padding: 0px 72px 0px 0px;
  }
  
  #content .brick{
    position: relative;
  }
  
  #content .brick .close{
    position: absolute;
    right: 8px;
    top: 8px;
    color: #616161;
  }
  
  #content.pages .brick.title{
    height: 120px;
    border-left: 8px solid #34ABD7;
  }
  
  #content.pages .brick.identify{
    display: none;
  }
  
  #content.pages .brick.save{
    position: absolute;
    right: 0;
    bottom: 0;
    width: 64px;
    height: 54px;
    min-height: 54px;
    margin-right: 0;
    color: #fff;
    background: #158A53;
  }
  
  #content.pages .brick.close{
    position: absolute;
    right: 0;
    top: 0;
    width: 64px;
    height: 54px;
    min-height: 54px;
    margin-right: 0;
    color: #fff;
    background: #616161;
  }
  
  #content.pages .brick.save .icon, #content.pages .brick.close .icon{
    line-height: 1;
  }
  
  #content .brick.closed{
    width: 120px;
    height: 120px;
  }
  
  #content .brick.closed hgroup a{
    display: none;
  }
  
  #content .brick.closed form{
    display: none;
  }
  
  #content .brick form textarea{
    width: 100%;
    max-width: 100%;
    min-height: 200px;
    padding: 16px;
    border: 1px solid #666;
      border-radius: 0px;
    -moz-border-radius: 0px;
    -webkit-border-radius: 0px;
  }
  
  #content .brick form input[type="text"]{
    width: 100%;
    padding: 8px 16px;
    border: 1px solid #666;
    font-size: 1.5em;
    border-radius: 0px;
    -moz-border-radius: 0px;
    -webkit-border-radius: 0px;
  }
  
  
  @media all and (max-width: 799px){
    #content.pages .brick.close .text, #content.pages .brick.save .text{
      display: none;
    }
  }
  
  @media all and (min-width: 800px){
    header > hgroup{
      height: 120px;
      color: #fff;
    }
  
  
    nav{
      position: absolute;
      width: 250px;
    }
  
  
  
    #content{
      min-height: 100%;
      margin-left: 282px;
      font-size: 0;
    }
  
    #content .brick{
      min-height: 120px;
      min-width: 120px;
      background: #252326;
      background: #a93447;
      background: #F3F3F3;
      background-color: #e7e7e7;
      font-size: 16px;
    }
  
    #content .brick hgroup h2{
      display: inline-block;
      width: 80%;
    }
  
    #content .brick hgroup a{
      float: right;
      line-height: 1.13;
    }
  
  
    #content.pages .brick.controls{
      position: relative;
      padding-left: 136px;
    }
  
    #content > header{
      position: relative;
      padding: 0px 128px;
    }
  
    #content.pages .brick.identify{
      display: block;
      position: absolute;
      left: 0;
      top: 0;
      color: #fff;
      background: #34ABD7;
      width: 120px;
    }
  
    #content.pages .brick.identify .icon{
      display: block;
      height: 60px;
      width: 60px;
      float: none;
      margin: 0 auto;
      font-size: 5em;
      color: #fff;
      line-height: 1.25;
    }
  
    #content.pages .brick.title{
      border-left: none;
    }
  
    #content.pages .brick.save{
      position: absolute;
      right: 0;
      bottom: 0;
      margin-right: 0;
      color: #fff;
      background: #158A53;
      height: 56px;
      min-height: 56px;
      width: 120px;
    }
  
    #content.pages .brick.close{
      position: absolute;
      right: 0;
      top: 0;
      width: 120px;
      height: 56px;
      min-height: 56px;
      margin-right: 0;
      color: #fff;
      background: #616161;
    }
  
    #content.pages .brick.save .icon, #content.pages .brick.close .icon{
      line-height: 1;
    }
  
    #content.pages .brick.controls .icon{
      position: absolute;
      left: 0;
      top: 0;
      height: 120px;
      width: 120px;
      background: #34ABD7;
      color: #fff;
      font-size: 5em;
    }
  
    input[type='submit'][value='%']{
      position: absolute;
      background: #158A53;
      border: none;
      left: 0px;
      bottom: 0px;
      width: 60px;
      height: 60px;
      font-family: "ModernPictogramsNormal";
      font-weight: 100;
      font-size: 2em;
      color: #fff;
    }
  }
  
  /* status */
  .status-board {
    width: 600px;
    margin: 0 auto;
    background: rgb(255,255,255);
    border: 1px solid rgb(220,220,220);
    border-radius: 5px;
    list-style: none;
    padding: 0px;
    line-height: 50px;
    cursor: default;
    margin-top: 10%;
  }
  .status-board  li {
    height: 50px;
    border-bottom: 1px solid rgb(220,220,220);
    text-indent: 15px;
    color:black;
  }
  .status-board ul li:last-child{
    border: none;
  }
  .status {
    display: inline-block;
    float: right;
    height: 1em;
    line-height: 1em;
    margin: 17px 15px;
    text-indent: 0;
  
    font-family:  'Monaco','Consolas', 'Courier', monospace;
    font-weight: bold;
    font-size: 13px;
    text-transform: uppercase;
    border: 1px solid;
    border-radius: 3px;
    padding: 1px 2px;
  }
  .blue {
    color: #2791d9;
    border-color: #2791d9;
  }
  .green {
    color: #2ecc71;
    border-color: #2ecc71;
  }
  .yellow {
    color: #f1c40f;
    border-color: #f1c40f;
  }
  .orange {
    color: #e67e22;
    border-color: #e67e22;
  }
  .red{
    color: #e74c3c;
    border-color: #e74c3c;





    <nav>
      <ul>
        <li><a class="brick dashboard" href="#"><span class='icon ion-home'></span>Dashboard</a></li>
        <li><a class="brick pages" href="#"><span class='icon ion-document'></span>Pages</a></li>
        <li><a class="brick navigation" href="#"><span class='icon ion-android-share-alt'></span>Navigation</a></li>
        <li><a class="brick users" href="#"><span class='icon ion-person'></span>Users</a></li>
        <li><a class="brick settings" href="#"><span class='icon ion-gear-a'></span>Website Settings</a></li>
      </ul>
    </nav>
    
    <div id="content" class="pages">
    
      <header>
        <div class="brick identify">
          <span class="icon ion-document"></span>
        </div>
    
        <div class="brick title">
          <h2>Home Page</h2>
        </div>
    
        <div class="brick close">
          <span class="text">Close</span>
          <span class="icon ion-close"></span>
        </div>
    
    
        <div class="brick save">
          <span class="text">Save</span>
          <span class="icon ion-checkmark"></span>
        </div>
    
      </header>
    
      <div class="brick closed">
        <hgroup>
          <h2>Main Headline</h2>
          <a href="#" class="icon ion-close js-close close"></a>
          <form>
            <input type="text" />
          </form>
        </hgroup>
      </div>
    
      <div class="brick closed">
        <hgroup>
          <h2>About Me</h2>
          <a href="#" class="icon ion-close js-close close"></a>
          <form>
            <textarea></textarea>
          </form>
        </hgroup>
      </div>
    
      <div class="brick closed">
        <hgroup>
          <h2>Gallery</h2>
          <a href="#" class="icon ion-close js-close close"></a>
          <form>
            <textarea></textarea>
          </form>
        </hgroup>
      </div>
    
      <div class="brick closed">
        <hgroup>
          <h2>Page Settings</h2>
          <a href="#" class="icon ion-close js-close close"></a>
          <form>
            <textarea></textarea>
          </form>
        </hgroup>
      </div>
    
    
    </div>
    
    <footer>
    
    </footer>




<ul class="status-board">

	<li>
		<span>ROAD CONSTRUCTION</span>
		<span class="status green">resolved</span>
	</li>
	<li>
		<span>POLITICAL ISSUES</span>
		<span class="status yellow">on-going</span>
	</li>
	<li>
		<span>BRIDGE RECONSTRUCTION</span>
		<span class="status orange">Partial resolved</span>
	</li>
	<li>
		<span>EMBLEZZMENT OF FUNDS</span>
		<span class="status red">rejected</span>
	</li>
	<li>
		<span>Nuclear Reactor</span>
		<span class="status blue">Action Required</span>
	</li>
</ul>

<div class="graph-container">
        <div class="graph-titles">
         <!-- Populated -->
        </div>
          <div class="graph">
         
          <div class="graph-bars">
            <!-- Populated -->
          </div>
        
          <div class="markers">
          <!-- Populated -->
          </div>
		</div>
		
        <div class="graph-key">
          <div class="graph-key-item">
            <span class="graph-key-dot urgent"></span><span id="urgent-title">Urgent</span>
          </div>
          <div class="graph-key-item">
            <span class="graph-key-dot active"></span><span>Active</span>
          </div>
          <div class="graph-key-item">
            <span class="graph-key-dot newCount"></span><span>New</span>
          </div>
          <div class="graph-key-item">
            <span class="graph-key-dot newFromBatch"></span><span>New From Batch</span>
          </div>
        </div>
      </div>
      <button id="teamGraph">Team Graph</button>
      <button id="userGraph">User Graph</button>