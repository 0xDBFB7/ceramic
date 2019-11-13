Dan's Vacuum Wine-Tumbler Furnace

Just over a year ago, it became apparent that a certain project would require a custom ceramic composite. 

Proper technical ceramics all require sintering at above 1300c, and most fun applications require 1600C+. 
Unfortunately, the last 500c requires what I consider to be some nifty materials science because of Boltzmann's \sigma A T^4 and all that.
For instance, conventional heating element materials like nichrome and kanthal just give up around about ~1300 C - Kanthal very spectacularly so:

> The next factor investigated was the suitability of Kanthal A-1
> as heater material. Although this material is suitable for use to
> 1325 0 C in air, at least one reference does not recommend its use in
> vacuum at temperatures over 1000°C. This warning is founded in the
> rapid evaporation of a component (chromium?) from the alloy and verified
> by tests we performed on bare wires in ultra-high vacuum. Sample
> filaments burned out after two hours or less at a surface temperature
> of 1200°C.

<https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19760003136.pdf>

<https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20080013560.pdf>


I therefore find myself in the very strange and somewhat enviable position of having incidentally built a 1700 C furnace which costs a miniscule fraction that of
existing solutions. 

So I'm left with something of a spin-off project: a furnace was built with a SiC element capable of 1,400 C for $50, and a little polishing turned it into a 1700 C vacuum.

Considering that commercial kilns cost about $(1000 + T^3), I figured this
 could be of some utility to others, so I'm planning on selling a more polished version of the same for no very good reason. 

The idea is primarily "if Mr. Musk can sell flamethrowers to fund a tunnel, maybe I can sell a furnace to fund a particle accelerator", 
but don't buy it for that.

I would greatly prefer to do this when all is said and done and I have some pretty pictures of the product to show. Unfortunately, university dicates that I cannot spend time polishing this to a commercial level if nobody would be interested.

Specs: 

- $300 CAD.
- Off-the-shelf supply of Silicon Carbide element from commercial hot-surface-igniters, used in central heating; 
		plentiful supply, generic, obselecence unlikely, replacements $26.
		Element lifespan in oxidizing atmosphere: 100 hours/(1300-t^3) INSERT GRAPH FROM PAPER
		Element lifespan indefinite in N or Ar atmosphere.  
- 1,700 C low-vacuum[for now].
- Atmospheric 1,400c (degradation of element).
- Temperature measurement through SiC filament by measuring bandgap energy via resistance.
- Pressure measurement through penning-style thermal resistance.
- D-shaped bore, 30 mm ID x 200mm long (40 mm bore minus heating element volume). 
- Practice for some techniques which will be used by the [].
- Insulation based on satillite multi-layer insulation, using hard in-situ-sintered concentric non-fiberous alumina shells.
		If square, can self-sinter; probably useful.
- Programmable temperature profiles and ramp-rates.   
- Entirely open-source; plans, notes, recipes for all ceramics used, etc can be found on the github.
- Heating rates up to 1,000 C/min, and as low as you want.
- 1/3 to 1/10th the cost of equivalent products, but 5x the cost of building your own.
- If you don't find it very useful, that's on me: guilt-free no-return refund at any point in the future.

Applications:

- Sintering vacuum-quality porcelain/kaolin-composite insulators. [recipe]
- LTCC/HTCC tape-cast ceramic PCBs (the same technique used for ). [recipe]
- 96% Al2O3 insulators gel-cast in 3D printed molds []
	With this process, one can go from design to ceramic part in about 1 hour. 
- Vacuum brazing. (requires vacuum and N or Ar backfill)
- Making sapphire. (requires vacuum and N or Ar backfill)
- Making nitrides.
- Making glasses.
- ???
- Burning bridges.

Limitations:

- You can build a 1300 C furnace

- I don't urgently need the money. Please don't sign up
	I feel kind of weird making money off this, since it's pretty simple to build. On the other hand, it costs $300 where everything else costs >>$1000.
- There are better, faster, cheaper techniques to create ceramic parts, like cheap microwave sintering or field-assisted/spark-plasma [thanks ice9!]
		[To date, science has not figured out how FAST is so effective.] sintering.
	I needed a general-purpose >1500c multi-atmosphere sintering setup, but if you have specific requirements you can almost certainly do better than this.
- There's really no need to buy this from me. I'm making money off this; if you value your time less than $100 
	it makes more sense for you to build one; especially if all you need is 1400 C and air atmosphere.
	The only possible 'novelty' of this device is in the use of off-the-shelf heating elements, which 
	you can take advantage of without me as your middle-man.
- Small bore.
- Vacuum pump not included. A $150 refrigeration compressor should do. 
- "Good work! I wish to support this by purchasing your furnace."
	Don't! I forbid it. I don't deserve it. Build it yourself and give the money to charity or whatever.
	Please only purchase this if you think the marginal value of a pre-built furnace
- The silicon-carbide element degrades to carbon monoxide bubbles rapidly with operation at above 1400c in atmosphere; high temperatures require an argon or nitrogen backfill
	 	(which isn't difficult). This failure mode is the same as that seen on the silica-conversion-coated 
	 	reinforced-carbon-carbon panels on the leading edges of the Space Shuttle. 
- Safety concerns:
	High temperatures can hurt.
	If you put something into the chamber that pyrolyzes to something toxic (Borax -> boron gas), you will die.
	If you put something into the chamber that produces metal vapor, you will get metal fume fever and possibly die.
	There are standard inert gas asphyxiation risks.
	If you don't inert the atmosphere, the interlocks fail, and you have no ventilation,
		 the chamber will fill with carbon monoxide from the decomposing SiC element, and you will die.
		 
	Main concerns with recipe ingredients:
		If the Alzheimer's hypothesis is to be believed, exposure to unbound alumina dust will make you dumb.
			This is unlikely to be true. See this recent review.
		Titanium dioxide has recently been re-classified as a carcinogen.
			This has only been demonstrated in nano-scale titania, or by 
		Silica fume from kaolin. 
	
- I am an *idiot*. I wasted *weeks* thinking poly(vinyl acetate) was the same as poly(vinyl alcohol). I wasted an equal *weeks* trying to make jello.

What am I getting into?

- I have some experience in the difficulties of production design from my last business (SafeSump Inc.). This won't be a simple affair. 
- This is practice in logistics for when *the real deal* is finished, hopefully 1 to 2 years from now.


Machining and assembly will be done by some good friends at Kesti Machining. They need the work.



[Order]