# Ceramics as she is spoke

> The difference between science and screwing around is writing stuff down.

\- *Adam Savage*

> Do what you can, where you are, with what you have.

\- *Akin's 34th law*

[TOC]

### Issues with this article

- I'm an idiot with no experience in ceramics. You could do better.
- This project was under considerable time pressure while attending university, and so was not nearly as rigorous as it should have been. I overcomplicated everything, made inane mistakes like using the wrong mix ratio for several months, etc.
- I had a total budget of <$300. This constrained the solution extensively.

### A note on safety

Below, some common-sense paranoia:

Like most inorganic dusts, aluminum oxide powder isn't all that good for your respiratory system. It's not nearly as damaging as silica, but a respirator or fume hood is recommended. There have also been a few studies showing some (admittedly tenuous) connection between aluminum inhalation and Alzheimer's.

The Kaolin clay and optional CF reinforcement fibers have similar dangers. See @yoder2015carbon.

It must scarcely be said that fire is almost certain while working at these temperatures. Don't leave anything unattended and have fire extinguishers nearby.

just If using a lost-PLA process, beware decomposition products. Perform the bakeoff and sintering steps in a well-ventilated area.

Green bodies are wont to explode. This will send superheated ceramic shrapnel in all directions. 

Finally, contact with 230v kiln elements will almost certainly be lethal. Keep that in mind; I didn't.



![20190518_142932_HDR](../../ion_printer/media/20190518_142932_HDR.jpg)



# The recipe

This is process 5, taken almost verbatim from 

Previous trials; the most successful of these failures is process_4.

Limitations:

- For production use, FAST or SPS is almost certainly more effective. See FAST.

  - Thanks to ice9 on twitter for leading me to SPS.


1. 







## And now, an infodump of blather

### Preamble on motivation

A few months ago, it became apparent that a certain future product would require several thousand high-voltage insulators. These insulators would need to withstand ~1500c continuously while remaining safe in high vacuum, and be rapidly produced in-house with arbitrary geometries. 

Additionally, the economics of the product dictate a per-part cost of under $0.03.



#### Machinable ceramics

Macor

#### Castable ceramics

[^macor]: Rescor, Macor 780 et al [External](http://www.cotronics.com/vo/cotr/pdf/onepg700.pdf)

Cotronics carries a lineup of castable and machinable ceramics, some of which fulfill the temperature . None fulfill the cost or vertical integration requirements.

#### Porcelain

Porcelain is an introductory ceramic, with a low firing temperature of ~1200-1400c. This is readily available for 

The temperature resistance of 



## The green binder

As with most powder sintering processes, the process starts by creating a green body. Much like trying to bake a cake with nothing but flour, one can’t generally pour alumina into a mold and fire it; cohesion requires intimate contact between grains, and even the slightest of internal stresses will cause it to crumble. A binder is required that will maintain structural integrity 

Note that this is not true of FAST/SPS.

#### Pressing

[^pressing]: @ nptelpressing - https://nptel.ac.in/courses/112107085/module3/lecture5/lecture5.pdf

Pressing the powder sidesteps these cohesion issues, making a green of reasonable strength without any binder. You can either make an aqueous slurry (wet pressing), or just compact dry powder.  

Many sub-techniques are available: wet, dry, hot, etc.

Unfortunately, a CNC mill capable of cutting hard dies to reasonable tolerances and finish quality was not available. In addition, the pace of iterative testing is limited by how quickly new dies can be made.

A few attempts were made at pressing with 12L14 dies, the hardest material workable with the equipment available; the parts created were acceptable, but granular jamming and die deformation rapidly destroyed the mold.



#### Slip-casting

Perhaps the simplest process to create ceramic green bodies, [slipcasting](https://en.wikipedia.org/wiki/Slipcasting) entails pouring a fluid solution of porcelain into a hygroscopic plaster mold. 

In addition, the plaster mold must be dried for many hours before it is sufficiently absorptive to allow the slip to gelate. This process can be accelerated by maintaining a flow of hot, dry air over the mold. The mold cannot be heated above 49 C, however, as the surface will begin to calcine. 

Microwave drying of plaster is conveniently self-limiting.

This also introduces a 

https://www.usg.com/content/dam/USG_Marketing_Communications/united_states/product_promotional_materials/finished_assets/usg-no1-pottery-plaster-data-en-IG1366.pdf



There’re a few different ways of making this green body.

<style>p.seven {
  border-style: solid;
  border-width: 20px 10px 10px 10px;
    }</style><p class="seven"><b>I feel like I learned something:</b><br>When characterizing trial-and-error processes, it might be useful to think of R&D in terms of software unit testing; that is, you want to create a sort of <a href=https://stackoverflow.com/help/mcve>MCVE<a></a> of your controls. As an example, it may be helpful to use the smallest batch size and the simplest test coupon likely to exhibit the same behavior as your final product. In this particular case, I began iterating the alumina recipe using my desired full-size feedthough part, where a simplified test coupon would have required much less drying time and consumed 0.05x as much alumina - allowing me to try dozens of variations within the same batch.<br><br>On the other hand, making your test coupons overly simplistic may lead you down inconsequential paths of inquiry. Had I not used a coupon with a cavity, I would likely not have discovered some difficulties inherent in casting perfectly void-free paraffin molds. It's a subtle tradeoff! I guess you just have to use your best engineering judgement.<br><br>This is probably obvious to all who know what they're doing - a select few whose ranks I am most definitely not a member of.</p>

### An aqueous suspension

Aluminum oxide isn’t soluble in water to any meaningful degree, but any sufficiently fine powder will disperse into a suspension purely through Brownian motion. 

There are a few sources that describe[^citric] the use of citric acid as a dispersant to improve the homogeneity of the colloid. No significant effect was observed in these tests.

[^citric]: Garrido, L. B., and E. F. Aglietti. "mullite-zirconia COMPOSITES: Effect of dispersants on slip and cast properties."

The cohesive forces between alumina particles are negligible at low temperatures, and so a binder must be used. The precise mechanism by which the binder operates at extreme temperatures is not known to me.

When this type of suspension is available, a few more options arise.

#### Freeze casting

@ koch2003evolution





#### Gel casting

You can also mix in some kind of binder that will burn off when fired. Any organic binder with the following properties would be a suitable candidate:

- low viscosity to flow into the mold when mixed with your ceramic powder 
- strong when cured or dried to be cleanly extracted from the mold
- well-behaved while firing - able to cope with the severe thermal stresses without allowing the green to shatter
- more prone to gentle sublimation and vaporization rather than violent decomposition
- usable at sufficiently low solid percentages so that shrinkage is minimized, both during drying and firing

Additional requirements were

- inexpensive and readily available
- 



- Alginate + calcium iodate [^@xie2001new]  (the iodate was not available in short order)

- Fancy water-soluble epoxies (tried regular epoxies, failed miserably as expected)

- PVA

- Dhara, Santanu, and Parag Bhargava. "Egg white as an environmentally friendly low‐cost binder for gelcasting of ceramics." Journal of the American Ceramic Society 84.12 (2001): 3048-3050.

  *Frankly, I’m as surprised as you are.*
  
- Freeze-casting

  ​	Despite its simplicity, this process was not tested. The crystallization that occurs when water is frozen can cause voids and high porosity in the final product. It was feared that this would lead to virtual leaks and contamination in a vacuum environment.



[^PVA]: Chabert, France, David E. Dunstan, and George V. Franks. "Cross‐linked polyvinyl alcohol as a binder for gelcasting and green machining." *Journal of the American Ceramic Society* 91.10 (2008): 3138-3146.
Fluffy, delicious organic binders, specifically.




> oh the redhead said you shred the cello, and I'm -

#### Jello

[^4]: Stoner thermoplastic mold release, McMaster-Carr #1409K44 [External](https://www.mcmaster.com/1409k44)

I was not able to replicate their process after many, many attempts. The fully gelated green body was far too delicate to be removed from the mold, was excessively porous. This is certainly not due to any failing on the part of the paper's authors, but almost definitely some unknown in my experimental setup.

However, a modified process was discovered that was found to be quite effective. It involves drying the gelated body at a significantly elevated temperature.

<video src="../media/20181110_213428.mp4"></video>

When poured into a small test tube, the mix ratio was very obviously excessively wet.

The amount of gelatin used was too low to reliably measure on my $14 milligram balance.



at this juncture I would like to point out the existence of the Gelatine Handbook[^4]. 350 pages of excruciating detail on every possible intricacy of the gelatine production process. 

[^4]: Gelatine Handbook [Internal](../references/Gelatine_Handbook_tagt.pdf)  [External](https://www.docollection.me/doc/Gelatine_Handbook_tagt.pdf)

Of Englishe dogges: the diuersities, the names, the natures, and the properties https://books.google.fi/books?id=y8kCAAAAYAAJ&pg=PP7&hl=en&authuser=0#v=onepage&q&f=false



Something quite interesting can be observed with this open-cavity mold. No meniscus is present.

Drying at 70c, however, produced a very strong green body:

<video src="../media/processed/20181110_143321.mp4"></video>



#### Molds

#### Dry-green machining

It is often useful to machine a part when dry. A greater dimensional accuracy can be obtained this way.



#### Drying

Different cross-sections tend to dry at different rates, causing a differential expansion and contraction. At 70c, the thin mounting lobes on the part above invariably cracked before the entire body was dry. 

Wood glues typically have a solids percentage of 40-70%.

#### Bubbles & Porosity

The USP pottery plaster that I used for my porcelain tests recommended mixing with high energy. 

I inexplicably mentally transferred that requirement to my alumina tests, which led me to, er, *whip* the alumina slurry. 

<video src="../media/processed/20181121_134556.mp4.mp4"></video>

This process might actually be useful for producing a sort of low-density insulating alumina foam; the rheology of the gel leads to a very porous structure. It also represents the antithesis of my desired end product.




<video src="../media/20181121_135626.mp4"></video>

Degassing pseudoplastics like gelatine causes an annoying feedback loop: as the moisture evaporates, the solution is chilled, which greatly increases the viscosity, making the solution ever harder to degas.

https://abbess.com/wp-content/uploads/2016/03/Degassing-Mixing-V2-Secure.pdf

In any case, stirring the colloid gently a few times was more than sufficient to produce a homogeneous suspension of alumina, and this process was abandoned. The final PVA-binder process does not require degassing.

## The refractory binder

#### Clay



#### Manganese dioxide

[^mno_patent]: Luks, Daniel W. "Vitreous high alumina porcelain." U.S. Patent No. 2,290,107. 14 Jul. 1942. [Internal](../references/US2290107A.pdf)

[^2]: NileRed on Carbon-Zinc batteries [External](https://www.youtube.com/watch?v=XC5q9mDKUCo)

I am quite critical of the patent system. Despite having a patent pending, I am   

But this patent is prime example of how the system could work. This dude ran nearly 4500 tests.



Luckily, $$MnO_2$$ is readily available in an impure form in carbon-zinc batteries.[^2] I ripped a few apart



## Kiln in the name

Now we come to the matter of heating the green to the sinter temperature.

The majority of clays and porcelains fire at pyrometric cone 4 to 8, corresponding to a peak temperature of approximately 1186c to 1263c. 

The sinter temperature of pure alumina appears to be a matter of some ambiguity, but reasonable strength  generally requires 1700c. This is well past the cone scale entirely.

However, the addition of silica or clay precipitously decreases the required temperature. 

The amazing Ben Krasnow has an excellent treatment of the pyrometric cone system and the basics of refractory science in his video on glass production.[^krasnow_cone]

[^cone_chart]: [External](http://www.overglazes.com/PDF/Orton-Cone-Chart-C.pdf)
[^krasnow_cone]: [External](https://youtu.be/mUcUy7SqdS0)

#### Gas firing

If the part in question is sufficiently small (within ~7 mm^3), one may find that a bunsen burner or propane or oxy-acetylene torch can be used to fire. Extremely small parts (~2mm)

This method requires practice and finesse, is tedious, and produces a low-quality product. Temperature gradients.

Given the low cost of the kiln described below, I do not recommend this method. 

I have observed that a distinctive white glow can be seen when sintering has been successful.

Without the insulation of a kiln, the emissivity of the part becomes a concern. Graphite molds or crucibles repress heating significantly due to their high epsilons. This is not an issue in a furnace, as radiated power is absorbed and re-emitted by the kiln walls.

The sensitivity of the green during firing cannot be overstated; after the binder is burnt, even the slightest shock or breeze from the torch can destroy it. It is recommended that a firebrick be used to provide a stable, shock-free heating surface - unlike the majority of my testing, which was performed on tungsten rods. 

#### Electric kilns

#### Dan's silly SiC kiln

Commercial zirconia sintering kilns typically use Silicon Carbide elements. These can withstand ~2500c in a vacuum, and. 

Furnace heaters use Silicon carbide Hot Surface Igniters. These are readily available for $25 on Amazon, and can reach 1700c.

These have a reputation for being very delicate; however, the element used in my kiln was soiled greatly by splattered debris, was run for hours continuously, and overvolted significantly.

Silicon Nitride igniters are also available. 

I have often found that the rate of iteration; in the software world, a 30-second compile time or unit test time is not acceptable; so why is it desired here?

Total cost is around $50. At 135v, this design can reach 1300c in under 1 minute, and 1500 in ~3 minutes. It appears to survive well for several hours at this temperature; and no SiC element wear has been observed.

I was concerned that the low-frequency; this is a concern with Peltier elements, for instance - and was planning on building an overcomplicated bridge-rectifier. However, my fears were completely unfounded.

#### Stock ceramics kilns

A birthday gift from my outrageously resourceful parents:

<video src="../media/20181111_162140.mp4"></video>

This surplus ceramics kiln ($50) draws 5.5 kilowatts while operating. It can reach roughly 1300 C in under 3 hours.

Most of the elements were broken upon receipt. Thin-gauge 220v 1-2 KW nichrome elements[^elements] can be had for cents on eBay; while these were clearly not equivalent to the original heavy-gauge heaters, they performed satisfactorily.

[^elements]: [External](https://www.ebay.com/itm/Kiln-Furnace-heating-element-Resistance-wire-220V-2000W/332157782488?epid=737709198&hash=item4d562589d8:g:4AwAAMXQTT9RsLj-&frcectupt=true)

#### Molybdenum disilicide

No high-temperature lab would be complete without a Molybdenum disilicide kiln.`zirconia sintering kiln`seems to be a useful keyword. These are, however, many thousands of dollars.

#### Vacuum furnace

If convective cooling can be eliminated, heating these small parts becomes quite simple. Assuming a generous surface area of 5 cm^2, the Stefan-Boltzmann law indicates 
$$
\text{P}=\text{R} \text{E} \text{A} \text{T}^4 = 5.67\times10^{−8} \times (1800 \text{K})^4 \times 0.5 \times 0.0005 m^2\approx300\text{ watts}
$$
That's really quite insignificant.

However, at 5% the thermal conductivity of copper, transferring heat from a thin tungsten heater to the bulk of the ceramic is quite a difficult task.

In addition, my high vacuum chamber was not serviceable during this period, forcing me to use my low-vacuum chamber, which can only attain a vacuum of around 50 Pa - not nearly sufficient for this process. This was assembled 2 hours before leaving for finals, and it looks the part.

As a quick test, HP 6428B 45A PSU

<video src="../media/20181211_173959.mp4"></video>

Smoke is very interesting at low pressures.

I used the vacuum inlet as a high-current feedthrough. Joule heating caused some consternation.



#### Gas firing

After . Lo and behold, the fragment took on the desired glassy texture and increased in strength considerably. 



I supported the part with some 3/32" Tungsten TIG rods. 

#### Electric arc furnace



# Measuring temperature

McMaster carr thermocouple

The values from this thermocouple

#### Optical pyrometry

Disappearing filament

"Selective Radiator". http://gsp.humboldt.edu/olm_2015/courses/gsp_216_online/lesson8-1/emissivity.html , 

The spectral emissivity of alumina looks like someone dumped overcooked pasta into matplotlib. 

For this reason, many early pyrometers filtered 

# Grinding

Alumina is very hard - a Mohs 9. A standard diamond-bladed wet tile saw was not effective at cutting or grinding off-the-shelf alumina. Some have demonstrated scoring and breaking large sheets.

# Brazing

#### Anodic bonding / electroadhesion

Followers of my youtube channel will have learned of my brief affair with electroadhesion. While easily achievable with glass/copper interfaces, I was curious as to whether this process would be practical to perform with alumina. And indeed it is! I have found precisely one mention of successful anodic bonding to the beta allotrope/phase of alumina, leading me to believe that this process is beyond my capabilities and patience. [paper here]. 

https://ceramics.onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.1979.tb12726.x

one more paper though

# Anodic bonding



Cutting 





# Wanna chat about this? Hit me up on twitter @0xDBFB7, or on irc.0xDBFB7.com:6667 #general.

[^operating]: Opening an operating kiln is extremely ill-advised: the thermal shock sent small chips of superheated refractory brick in all directions. Putting your arm into a 600 degree kiln in a crude attempt at brazing aluminum is not at all advisable. Putting your arm into said kiln while wearing a polyester jacket is positively insane. In unrelated news, I have a new jacket.