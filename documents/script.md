Hi! Let's talk ceramics.

A few months ago, it became apparent that something I've been working on would require a few thousand vacuum-safe high-voltage insulators, capable of surviving service temperatures above around 1500c. This is quite a substantial requirement, and only a few materials are suitable. Of these, only aluminum oxide (or alumina) seemed to be achievable for the monetarily limited.



I know what you're thinking; why not a machinable ceramic like Macor? The economics of this thing only work out if these ceramic parts can be made for less than a few cents, and machinable ceramics typically cost some $30-50 for a few hundred grams. Finally, vertical integration is the best thing since sliced silica.

The process that I'm about to describe requires a \$50 kiln plus   \$15 per kilogram of ceramic.

All in all, I learned a bunch, wasted a lot of time on inane avenues of investigation, did a bunch of dumb things, and overcomplicated everything to a degree previously only found in college textbooks.



I'd like to preface this by stating that I'm not a materials scientist. Also, this is going to be almost entirely empirical; I don't have a theoretical basis for this work. Also, nothing I'm about to show is even remotely my invention, I'm just poorly implementing the work of several papers.



Also, if you're planning on doing this in production, please ignore the process I'm about to describe; Field-Assisted Sintering is arguably a much better method. More on that later.



The process I'm about to describe is almost verbatim from this paper with a few simplifications; I've tried a number of different methods and this seems to be the most reliable one that's still easy to achieve. I'm going to gloss over a number of important details; if you're going to try this process, I recommend skimming through the references in the description.

You should definitely wear a dust mask throughout; some of these ingredients can give you a bad case of the lung cancers if you work with them on a regular basis.



First, you want to simplify the designed geometry of the part as much as possible; this will save you a world of pain in the future. Thin or varying cross-sections will tend to crack while drying, due to differential expansion - this is pretty much universal advice in ceramics, by the way.



Now, add 10 to 30% Kaolin clay. In general, purer alumina parts have better properties across the board, like temperature resistance; however, the sinter temperature also needs to be that much greater to get acceptable strengths. Pure alumina often requires 1600c for two hours, while 30% kaolin seems to depress that to around 1350c for 20 minutes. 

Interestingly, this is not reflected in the paper linked; they stopped getting a density improvement over 1400c, even with pure alumina.

This is pure calcined alumina powder; I'm not sure what the grain size is, but it's really fine. Most technical ceramics use less than 3 micron grains.

I would really recommend keeping the Kaolin percentage between 70-80%; beyond that, it gets pretty annoying, everything breaks extremely easily, and you need crazy temperatures to get a usable part. 

Even at 70%, however, this stuff is ludicrously temperature-resistant - it can easily withstand 1500c. 



This is where you can season the mixture to taste; more on that later.

Chopped carbon fiber reinforced aluminum oxide composites sounds badass.

Mix the powders well; any inhomogeneity will of course appear in the finished product.



Now, if we added water and molded the part in its current state, it would just fall apart immediately before reaching the sinter temperature - much like a cake baked with nothing but flour. We now need what's known as a green binder; something that will burn off cleanly at temperature,  ----- . Many organic binders are suitable, (more on that later), but I highly recommend white PVA wood glue (this stuff specifically).

You want to add x% of this - that is, add 0.4g for every 10g of alumina+clay.

For reference, these white glues typically have a solids ratio between 45 and 70%.

You can play around with this percentage; in general, a lower percentage will increase fired density, but will be much more difficult to work with; the green strength will go down precipitously.

The paper this is based off of then added a PVA crosslinker, but this doesn't seem to be necessary.



Now we add water. About 15% by mass of the solids seems to work well, but it evaporates so quickly that this is best done by viscosity; a putty-like consistency seems to do the trick. Note that alumina is 4 times as dense as water.

At this point, you can form it with a machined delrin or graphite or 3d printed mold, cast it in urethane (you can use glycerine to set silicone if you don't have urethane), or really any other conventional molding method. It's best if the mold is made in three parts, for ease of ejection. Delrin is a great material for this because of its low surface energy; almost nothing sticks to it.

You can even let it set in the mold, but it becomes very brittle and difficult to eject without damaging it. You can mold it in graphite and leave it in the mold while firing; but that usually makes it shatter; also, graphite degrades greatly over 800c in atmosphere, so it's pretty much one-use-only. 

Coating graphite molds with a silicone oil causes a protective layer of silicon carbide and silicon dioxide to form at high temperatures. Haven't had any success with this, but apparently it's quite useful - anyhow, I digress.

A syringe works well to inject into the mold.

I've also had good luck with this "cookie-cutter" type of mold. 

This process is called gel-casting.

Alternatively, you can form it into a rough ingot, let it dry for 3 hours, and then CNC machine it. This has the advantage of nulling out the 3 or 4% shrinkage that usually occurs while drying.

This stuff machines really well, similarly to graphite. As you'd expect, the cutting forces are essentially zero, so you can get a good finish quality. This is a 1/16th inch carbide tool at 24,000 rpm doing 100 mm/min.

You could also thin out the putty further, and use it a dip coating for metals. If you use a propane torch to sinter, this even works on aluminum, since the alumina is so insulating that it hits 1300c before the aluminum hits 700 c.

You can also thin the solution further, and deposit an insulating layer via a process called cataphoresis, a variant of electrophoresis. This is commonly used for indirectly heated cathodes in vacuum tubes. See this paper for the details on that.

If you want a really thin solution and you find that the alumina isn't dispersing, you can try riot gear, or add some citric acid. 



Once you have the dried green body, you need to fire it. 

The paper 

Most importantly, however, it only takes about 1 minute to get to 1500c, allowing for very fast iterative testing. I've found that the lag time between new information and experimental data is a strong predictor for success in my style of research.

For the last few decades, gas central heating furnaces in homes have used hot surface igniters to light the burners rather than spark ignition; apparently, this provides a more reliable ignition.

These have a reputation for being very delicate, but as you can see this one has been quite throughly soiled by ceramic and run continuously for half an hour or so, and it hasn't broken. There are more resilient Silicon Nitride igniters, but these seem to be less temperature resistant, with teflon insulation. Silicon nitride sublimates at 1800c, whereas Silicon Carbide melts at some 2700c. The SiNi ones also require an 80v DC supply for some reason, though haven't seen any discussion as to why that is.

These are generally designed for intermittent use (cycles of 20 seconds or so), but the body is made from Steatite C220, which is good to 1700c, the wire insulation is fiberglass, and the wires themselves are made from nichrome 80. 



The SiC element does degrade; after running for about 40 minutes at 140v I noticed some very strange bubbling, which is apparently a known issue with carbides; if I understand this correctly, apparently this is a pretty complex multi-stage phenomenon; first, the carbide oxidizes to silicon dioxide. This dioxide then reacts with the original carbide to form silicon oxide, which evolves carbon monoxide gas in the interface layer. This inflates a molten bubble of the silicon dioxide layer. Very cool - I guess this means you probably shouldn't run this overnight in your bedroom.



See @raj2015 for details.



This seems to be a largely cosmetic issue, however; I've put about 10 batches through this kiln so far and haven't seen any change in performance. At $25 per element, I'm not super concerned if it's destroyed in short order; I can probably make a few hundred parts in this volume before it goes.

Previous concoctions using different binders were sensitive to the temperature ramp rate; anything over a few dozen degrees per second would shatter the part. I used to have a SSR and a little PID loop to control the ramp rate and peak temperatures; however, all my thermocouples have now melted, and the PVA binder seems to be unconcerned by even the crazy dt/dts that this oven can hit at max power.

The PID coefficients depend on the thermocouple, of course, but 1,1,6 and windup limits of -300,300 seems to be a good start.



Tonsil A: alternative heat sources

For very small parts with simple geometries (component lead insulators, for instance), you can fire with nothing but a propane torch or bunsen burner. There's a distinctive white glow that seems to occur when the proper sinter temperature has been reached; I think this is an effect of the translucency of solid alumina compared to the powder form.



However, getting reasonable strengths with anything larger than a few milimeters usually requires at least 10 minutes at temperature, as sintering doesn't just depend on the peak temperature; it's a non-linear temperature-time product that really does it. 

See Ben Krasnow's glass-making video for a better explanation of the pyrometric cone system.



If you're feeling really adventurous, you can try firing with an oxy-acetylene torch. 



I really can't recommend either of these methods, however; they're very finicky, and you can't put any process controls on them. Temperature gradients across the green body will usually make it explode.

I've tried using graphite molds as a heat spreader to alleviate some of these issues, but it's not effective at all; the differing coefficients of thermal expansion tend to crack the part, and the high emissivity of graphite tends to prevent you from getting to the required temperatures, even with ludicrous heat input. 

[flamethrower]





Typical ceramics kilns 



The finished part is extremely hard - hardness of Mohs 9. Grinding 

Tonsil B: FAST

Field Assisted Sintering (otherwise known as Spark Plasma Sintering) is a process in which 



Tonsil C: Gel-casting



Tonsil D: Brazing and bonding

Wait, you can braze alumina? Sure can. This paper goes into the details, but the jist of it is that a few metals adhere strongly with alumina, primarily titanium. 

containing titanium can be deposited onto the alumina in a vacuum or in argon, usually followed by a layer of something inert like gold. The titanium reacts with the alumina and adheres strongly; after which conventional brazing methods can be used. 

Tonsil E:







