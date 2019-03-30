# Ceramics

> The difference between science and screwing around is writing stuff down.

\- *Adam Savage*

> Do what you can, where you are, with what you have.

\- *Akin's 34th law*

[TOC]

### Issues with this article

- I'm an idiot with no experience in ceramics. You could do better.
- This project was under considerable time pressure while attending university, and so was not nearly as rigorous as it should have been. Many refinements still need to be made; the process has very marginal utility in its current state.
- I had a total budget of <$200. This constrained the solution extensively.
- 

### A note on safety

Like most inorganic dusts, aluminum oxide powder isn't good for your respiratory system. It's not nearly as damaging as silica, but a respirator or fume hood is recommended. There have also been some studies showing some (admittedly tenuous) connection between aluminum inhalation and Alzheimer's.

It need not be said that fire is almost certain while working with these temperatures. Take precautions.

If using a lost-PLA process, beware decomposition products. Perform the bakeoff and sintering steps in a well-ventilated area.

The green body will almost certainly explode on the first few attempts. This will send hot ceramic shrapnel in all directions.

Contact with 230v electric kiln elements will almost definitely kill you.

A consequence of haste can be seen here.

# The recipe

Limitations:

* See [the finished product](#the finished product) to see if the part quality is sufficient for your needs.
* This can only function for parts smaller than ~$5 \text{cm}^3​$ due to differential heating. An [alternate heat source]() would alleviate this requirement.
* Expect 0.5% shrinkage in X/Y; accurate Z (along mold gravity vector) may require grinding. 
* Vacuum-safe (volatiles are removed, as almost all carbon-carbon bonds are broken), but highly permeable. 
* If you have a CNC capable of machining steel dies, pressing may be a more desirable route.
* This is by no means an optimal process, just one that was attainable in my lab.

<hr>

1. **Print a PLA negative mold of the part you'd like to produce.** 

   I was not able to overcome Z-axis shrinkage, and so extended the mold vertically to allow for settling - standard reservoir/sprue arrangements did not work for as yet unknown reasons. Avoid ceramic walls of inconsistent thickness, as they will likely crack while drying. 

   A test coupon that I had good results with is available here[^coupon]. 

   Thicker PLA walls will reduce deformation during drying, but will increase the likelihood of cracking during burnoff.

   ![mold](../media/mold.png)

2. **Mix 1 volume $\text{Al}_2\text{O}_3$ with 1 volume warm water.**

   You may need to reduce the water volume if excessive Z-axis settling and shrinkage is observed while drying. 

3. **Add approximately 0.5 wt. % gelatine.**

   The solution must have a sufficiently low viscosity in order to flow into the mold without resistance while simultaneously retaining sufficient green strength for firing. This value may require tweaking.

4. *(optional)* **Add up to 5 wt.** **%** $\text{MnO}_2$ 

   *See [refractory binder](#The refractory binder).* *Sources indicate a sinter point depression, though no effect was observed in these tests*. 

5. **Add a refractory binder if unable to attain pure alumina sinter temperature (~2000c).**

   2.5 wt. % porcelain slip was found to be optimal[^slip]. Pure clay would be preferable; the dispersants in slip caused an undesirable meniscus effect. 

6. Add composite reinforcement to taste. 

   *see future additions.*

7. Stir gently until homogeneous and pour into PLA mold.

   *alternately, if a low thermal conductivity is desired, beat the hell out of the mix to form a foam.*

8. Dry in an oven for ~3 hours per cubic centimeter at well above the gelation temperature - roughly ~70 C.

   Urethane molds can generally tolerate roughly 80 C, whereas PLA will begin to deform at ~65c. The precise drying temperature depends greatly on the geometry of the part; again, variable thickness will cause differential drying and cracking at high drying speeds - see[^drying].

   In any case, the green must be thoroughly dry. Any residual moisture will cause it to explode.

9. Place the part in a graphite crucible[^8] or support it on tungsten wires.

10. Heat slowly with an oxy-acetylene torch to 500 C over the course of 1-2 minutes.

    The green is now too delicate to be moved without the support structure, so PLA burnoff must be done in-place.

11. Heat to approximately 1800 C with the torch. Hold temperature for 2-3 minutes. The entire part should glow white-hot.

    Determining the exact temperature is quite difficult and seems to be unnecessary. See [measuring temperature](#measuring temperature).

<hr>

Future additions: 

- [ ] Urethane casting
- [ ] Graphite heat spreader
- [ ] Quantitative sinter temperature measurement
- [ ] Lock down ideal gelatine percentage
- [ ] Carbon fiber cloth reinforcement testing

<hr>

[^1]: wt. % of alumina+water solution.
[^coupon]: `files/coupon_style_7.fcstd` https://github.com/0xDBFB7/ceramics
[^3]: [Internal](../references/)  [External]()

[^alginate]: Xie, Zhi-Peng, et al. "A new gel casting of ceramics by reaction of sodium alginate and calcium iodate at increased temperatures." *Journal of materials science letters* 20.13 (2001): 1255-1257. [Internal](../references/Xie2001_Article_ANewGelCastingOfCeramicsByReac.pdf)  [External](https://link.springer.com/content/pdf/10.1023/A:1010943427450.pdf)

[^1]: Sgobba, Stefano. *Materials for high vacuum technology, an overview*. No. CERN-TS-2006-004. Cern, 2006. [External](https://cds.cern.ch/record/983744/files/p117.pdf)

[^drying]: "The current empirically-guided drying process for parts which are about an inch thick can take several days, and is the longest stage in the gelcast manufacturing process." Ghosal, Sarbajit, et al. "A physical model for the drying of gelcast ceramics." *Journal of the American Ceramic Society* 82.3 (1999): 513-520. [internal](../references/drying.pdf) [External](https://www.scsolutions.com/wp-content/uploads/paper.gelcast2.pdf)
[^slip]: Sial 124M slip MSDS (~3.5% silica, ~20% kaolin clay) [Internal](../references/MSDS124M.pdf) [External](https://tuckerspotteryeshop.com/wp-content/uploads/msds/clay/MSDS%20124M.pdf)
[^8]: Readily available on eBay for $20.
[^9]: Green TIG rods are an excellent source



## And now, an infodump of blather

### Preamble on motivation

As an integral part of a future product, the marginal cost of these parts was a key concern. The design hinges on the ability to rapidly produce complex alumina geometries for mere cents.

Aluminum oxide is readily available and very inexpensive - the supplier I used charged ~$10/kg.

#### Glass

[reliable seal matching percentage] Kovar has a coefficient of expansion. Based off these data, some anecdotes I've heard on the difficulty of obtaining a reliably airtight glass-to-metal seal, and how electrochemically active glass is at high voltages, I figured 

#### Machinable/castable ceramics

[^macor]: Rescor, Macor 780 et al [External](http://www.cotronics.com/vo/cotr/pdf/onepg700.pdf)

Many of Cotronics' materials display quite severe outgassing values. Some anecdotes on Fusor Forums regarding permeability also seemed to concur with the assessment that these materials are generally not suitable for high vacuum.

### Mold and green binder

Unfortunately, paraffin melts at nearly the same temperature as the gelatine. This means that the gel must be almost completely dry (shrinking considerably) in the process.

Some problems with paraffin molds:

When casting fine details, it’s common for bubbles to form at the bottom. One way to fix this is to leave the heat on for a while, ensuring that the paraffin has time to flow into every nook and cranny. This, however, melts the hot glue sticking the mold together.

I guess I could just add a long sprue and reservoir to the mold to compensate for shrinkage.

Caulk/urethane molds

Caulking can be made to solidify quickly by way of glycerin.

## The mold and green body

Like most sintering processes, you want to start with a green body. Much like trying to bake a cake with nothing but flour, you can’t just put a bunch of alumina powder into a mold and fire it; there won’t be the intimate contact between the particles that’s required for cohesion, and even the slightest internal stress will cause it to crumble.

#### Pressing

[^pressing]: https://nptel.ac.in/courses/112107085/module3/lecture5/lecture5.pdf

Pressing alumina is a common technique. You can either make a slurry (wet pressing), or just compact dry powder. 

Many sub-techniques are available:

Unfortunately, a CNC mill capable of cutting hard dies to reasonable tolerances and finish quality was not available.

#### Porcelain

Perhaps the simplest process to create ceramic green bodies, [slipcasting](https://en.wikipedia.org/wiki/Slipcasting) entails pouring a fluid solution of porcelain into a hygroscopic plaster mold. 

There are a few limitations to this process. As you might imagine, part thickness 

In addition, the plaster mold must be dried for many hours before it is sufficiently absorptive to allow the slip to gelate. This process can be accelerated by maintaining a flow of hot, dry air over the mold. The mold cannot be heated above 49 C, however, as the surface will begin to calcine. 

Another interesting option is microwave drying of plaster, which is conveniently self-limiting.

This introduces yet another step where imperfections can arise

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

The cohesive forces between alumina particles are negligible at low temperatures, and so a binder must be used  - much like baking a cake with nothing but flour. The precise mechanism by which the binder can operate at well above 

When such a suspension is available, a few more options arise.

#### Freeze casting

https://link.springer.com/content/pdf/10.1023/A:1020718225164.pdf

Despite its simplicity, this process was not tested. The crystallization that occurs when water is frozen tends to lead to large voids and high porosity in the final product. It was feared that this would lead to virtual leaks and contamination in a vacuum environment; however, the gel-cast process appears to also lead to high surface porosity.

#### Gel casting

You can also mix in some kind of binder that will burn off when fired. Any organic binder with the following properties would be a suitable candidate:

- low viscosity to flow into the mold when mixed with your ceramic powder 
- strong when cured or dried to be cleanly extracted from the mold
- well-behaved while firing - able to cope with the severe thermal stresses without allowing the green to shatter,
- more prone to gentle sublimation and vaporization rather than violent decomposition (as was observed with PLA).
- usable at sufficiently low solid percentages so that shrinkage is minimized, both during drying and firing

Additional requirements were

- inexpensive and readily available
- 





- Alginate + calcium iodate[^alginate] (I couldn’t get my hands on the iodate in short order)

- Fancy water-soluble epoxies (tried regular epoxies, failed miserably as expected)

- PVA powder or Elmer's glue

- Dhara, Santanu, and Parag Bhargava. "Egg white as an environmentally friendly low‐cost binder for gelcasting of ceramics." Journal of the American Ceramic Society 84.12 (2001): 3048-3050.

  *Frankly, I’m as surprised as you are.*

[^alginate]: Xie, Zhi-Peng, et al. "A new gel casting of ceramics by reaction of sodium alginate and calcium iodate at increased temperatures." *Journal of materials science letters* 20.13 (2001): 1255-1257. [Internal](../references/Xie2001_Article_ANewGelCastingOfCeramicsByReac.pdf)  [External](https://link.springer.com/content/pdf/10.1023/A:1010943427450.pdf)

[^PVA]: Chabert, France, David E. Dunstan, and George V. Franks. "Cross‐linked polyvinyl alcohol as a binder for gelcasting and green machining." *Journal of the American Ceramic Society* 91.10 (2008): 3138-3146.
Fluffy, delicious organic binders, specifically.




> oh the redhead said you shred the cello, and I'm -

#### Jello

[^4]: Stoner thermoplastic mold release, McMaster-Carr #1409K44 [External](https://www.mcmaster.com/1409k44)

I was not able to replicate their results after many, many attempts. The fully gelated green body was far too delicate to be removed from the mold. However, I hit on a modified process that is quite effective. It involves drying 

<video src="../media/20181110_213428.mp4"></video>

When poured into a small test tube, the mix ratio was very obviously excessively wet.

The amount of gelatin used was too low to reliably measure on my $14 milligram balance.



at this juncture I would like to point out the existence of the Gelatine Handbook[^4]. 350 pages of excruciating detail on every possible intricacy of the gelatine production process. 

[^4]: Gelatine Handbook [Internal](../references/Gelatine_Handbook_tagt.pdf)  [External](https://www.docollection.me/doc/Gelatine_Handbook_tagt.pdf)

Of Englishe dogges: the diuersities, the names, the natures, and the properties https://books.google.fi/books?id=y8kCAAAAYAAJ&pg=PP7&hl=en&authuser=0#v=onepage&q&f=false



Something quite interesting can be observed with this open-cavity mold. No meniscus is present.

Drying at 70c, however, produced a very strong green body:

<video src="../media/processed/20181110_143321.mp4"></video>



#### Drying

Different cross-sections tend to dry at different rates, causing a differential expansion and contraction. At 70c, the thin mounting lobes on the part above invariably cracked before the entire body was dry. 



#### Bubbles & Porosity

The USP pottery plaster that I used for my porcelain tests recommended mixing 

I inexplicably mentally transferred that requirement to my alumina tests, which led me to, er, *whip* the alumina slurry. 

<video src="../media/processed/20181121_134556.mp4.mp4"></video>

This process might actually be useful for producing a sort of low-density insulating alumina foam; the rheology of the gel leads to a very porous structure. It also represents the antithesis of my desired end product.




<video src="../media/20181121_135626.mp4"></video>

A slight problem tends to arise when degassing pseudoplastics like gelatine. As the moisture evaporates, the solution is chilled, which greatly increases the viscosity, making the solution ever harder to degas.

https://abbess.com/wp-content/uploads/2016/03/Degassing-Mixing-V2-Secure.pdf



In any case, stirring the colloid gently a few times was more than sufficient to produce a homogeneous suspension of alumina.

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

Most porcelains fire at pyrometric cone 4 to 8, a peak temperature of 1186c to 1263c.

The sinter temperature of pure alumina is a matter of some ambiguity, but reasonable strength can be found at 1700c. This is past the cone scale entirely.

The amazing Ben Krasnow has an excellent treatment of the pyrometric cone system in his 

[^cone_chart]: [External](http://www.overglazes.com/PDF/Orton-Cone-Chart-C.pdf)
[^krasnow_cone]: [External](https://youtu.be/mUcUy7SqdS0)

#### Electric kilns

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



### Measuring temperature

McMaster carr thermocouple

The values from this thermocouple

#### Ratio pyrometry

I was planning on building a ratio pyrometer 

A problem arises when the emissivity of the substance varies throughout the frequency range - a "Selective Radiator". http://gsp.humboldt.edu/olm_2015/courses/gsp_216_online/lesson8-1/emissivity.html , but these 

Spectrometry





# The finished product

Here are the best parts I was able to produce.

![20181212_182620_HDR](../media/20181212_182620_HDR.jpg)



t's not going to win a beauty pageant, and it's almost definitely not sufficiently impermeable to be useful as a vacuum feedthrough. However, X and Y dimensional accuracy was superb, with only ~1% shrinkage. 0.3mm of the desired dimensions. Z dimensional accuracy was quite poor - the addition of slip increased the viscosity and caused a meniscus to form on the inside wall of the mold. 

As a light-duty refractory support, however, it's acceptable.



The shiny patch in the middle is molten glassy alumina, where I brought the torch far too close to the part. More rigorous process controls would be required in order to produce a truly usable part. Some sort of heat spreader would be excellent; I've since purchased a graphite crucible, which might improve the sinter quality. 

The two green lines are $WO_3$, residue from the 1/16" tungsten rods I used to support the part while firing.

![Screenshot from 2019-02-10 15-27-12](../media/Screenshot from 2019-02-10 15-27-12.png)

![Screenshot from 2019-02-10 15-27-45](../media/Screenshot from 2019-02-10 15-27-45.png)

![Screenshot from 2019-02-10 15-29-01](../media/Screenshot from 2019-02-10 15-29-01.png)

Kinda sucks.

In any case, I abandoned this project at this point. Alumina parts are a key component in a certain product that I am attempting to develop; I merely needed to convince myself that I would be able to vertically integrate this process within a certain timeframe.

I carefully sectioned (er, broke haphazardly) a few of the most successful parts. Here are a few micrographs of Batch 12 and 13.

![20181212_195540.mp440](../media/processed/20181212_195540.mp440.jpg)

Note the striations captured from the original PLA mold. Extremely fine feature definition and reasonably low porosity.

![20181212_195540.mp4](../media/processed/20181212_195540.mp4.jpg)

Here's the outside face.

I performed some digital strength tests:

<video src="../media/20181212_200256.mp4"></video>

The alumina had the strength of a particularly stale tea biscuit - a far cry from the results reported in the original gelatine paper. I hypothesize that this is due to my abysmal sintering setup, and not any fundamental mixture limitation.

Interestingly, the low-slip batch was noticeably stronger.

### Addendum: Grinding

Alumina is very hard - a Mohs 9. A standard diamond-bladed wet tile saw was not effective at cutting or grinding off-the-shelf alumina. Some have demonstrated scoring and breaking large sheets.

### Addendum: Brazing & bonding

#### Anodic bonding / electroadhesion

Followers of my youtube channel will have learned of my brief affair with electroadhesion. While easily achievable with glass/copper interfaces, I was curious as to whether this process would be practical to perform with alumina. And indeed it is! I have found precisely one mention of successful anodic bonding to the beta allotrope/phase of alumina, leading me to believe that this process is beyond my capabilities and patience. [paper here]. 

https://ceramics.onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.1979.tb12726.x

one more paper though



### Addendum: 

Cutting 



If you’re anything like me, sometimes you get a hankering for some homemade vacuum feedthroughs.

Vacuum, of course, requ

https://outgassing.nasa.gov/

http://esmat.esa.int/Databases/databases.html

If you want to  LIGO and CERN

 and you’re tired of those bland, lifeless Delrin insulators, what with their atrocious 0.43% TML [nasa page overlay]. And you definitely don’t want to go to the store and pick up some insulators

You can make a ceramic

When fully vitrified, both alumina and electrical porcelain are vacuum compatible.





Bake until golden brown.

Of course, I wanted to do this with what I had on hand.

>

So what you really want is some kind of organic binder that's both sufficiently low viscosity to flow into the mold when mixed with your desired ceramic powder, sufficiently strong when "cured" to be cleanly extracted from the mold, usable at sufficiently low percentages so that you don't get porosity or shrinkage after vaporization, and something that burns off cleanly when firing.

This shares some similarities with baking:

I mean, don’t let me near a stove.

Some examples are alginate with calcium iodate, fancy water-soluble epoxies, white PVA school glue, egg white. Okay, perhaps not egg white.

<https://s3.amazonaws.com/academia.edu.documents/46243057/j.1551-2916.2008.02534.x20160605-9566-1bhuice.pdf?AWSAccessKeyId=AKIAIWOWYYGZ2Y53UL3A&Expires=1541877772&Signature=0NrGbqgG1A8M3%2B9ZoBmqZkjXGmo%3D&response-content-disposition=inline%3B%20filename%3DCross-linked_Polyvinyl_Alcohol_as_a_Bind.pdf>

"Fabrication of alumina green body through gelcasting

process using alginate"

My favorite, however, is gelatine.



Porcelain slip generally relies on the plaster absorbing moisture from the material. In my case, the green would be far too thick to absorb the water anyhow. Porcelain shrunk significantly when drying at 85c. The green was almost perfect, except for the shrinkage. I bet a closed mold with a sprue and reservoir would fix that. However, Alumina has some properties that I need for other sections of the system, so I figured I'd drop porcelain for now and focus on that.

Glass is also sometimes acceptable. However, some parts of my chamber will have to withstand somewhere around 1600c, so having the ability to make ceramic parts would really be invaluable.

You can press and sinter alumina pretty easily. There's a number of sub-techniques here, with wet or dry die pressing, hot or cold isostatic, etc. The main limitation here is that you need to make press dies out of quite a hard material. You might be able to get away with aluminum for a few shots, but usually these dies are made of some sort of hardened steel. My dirt-cheap 6040 CNC is not going to cut it, what with its 50 thou chatter and whatnot.



Simple freeze-casting is possible, where an aqueous solution of alumina is frozen; however, crystal formation leads to high porosity and defects.

<>

As you might imagine, porosity is not particularly good in vacuum applications, as you'll get virtual leaks and contamination.

<https://www.osti.gov/servlets/purl/86933>

Alumina Casting Based on Gelation of Gelatine

At the end of the day, these alumina pieces actually have a tensile strength higher than that of 6061 aluminum.

0.5 vol of alumina, 0.5 vol water, 3% wt gelatin. Cured overnight in the fridge, though I think this was too long. Then I baked it at 70c for a few hours. The alumina layer seemed to settle to the bottom, forming a dense layer; a layer of water floated above. I'm not sure why.

<https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.1996.tb08006.x>

Gel-cast process 1



The paper details a 3% shrinkage during drying, and a 17% shrinkage during sintering.

This is way, way too liquid. I need a much higher alumina content.

The solution cracked in the mold significantly - I omitted the fridge step. I think the drying needs to be done a little slower. Some solution left in the mixing cup became an almost perfect texture.

I think the reason for the cracking is pretty simple: the corner radii on the mounting flanges dried far faster than the rest of the material.

Z shrinkage was pretty terrible. From a 5mm high fill in the mold, only 2.8mm remained - 44% shrink. I guess that makes perfect sense, given a 50% solids loading. My current hypothesis is that my aggressive drying procedure evaporates the gelatine, producing a heavily green part.

Green strength was pretty good; if the other issues hadn’t presented themselves I think these would have been fine parts.

Porosity was okay.



I should try using a delrin insert as the middle piece, and removing the mounting flanges.

I can use a seperate 3d printed piece for the back plate and all that stuff.

Use gelatin as the mold itself somehow? Nah, then it’ll melt at the same time as the cast part.

PARAFFIN WAX MOLD. Melt it away after drying. Temperature of 50-60c or so. Perfect. Or perhaps glue stick glue?

There was a lot of foam produced on the surface of the alumina slurry while mixing. I think it might be a good idea to add the gelatine after stirring in the alumina.

It might be possible to use two different types of wax.

I really should pick up some white glue. It would be much easier to work with a harder, higher-temperature green.

<https://wfs.swst.org/index.php/wfs/article/viewFile/101/101>

https://www.ebay.com/itm/Duco-Cement-Multi-Purpose-Fast-Drying-Nitrocellulose-Household-Glue-Cement-1fl/253819114889?hash=item3b18cc5589:g:yFQAAOSw~Ltbdpno:rk:1:pf:0



Tarnation.

If the wax stays hot for long enough, I could put the whole casting in the vacuum chamber...

Tried the vacuum chamber technique. As you might expect, it didn’t work; the paraffin boiled vigorously and large voids opened up.

Perhaps I need to turn the whole situation upside down, with the part at the top of the mold.

I also had considerable difficulty in removing the printed part.

Gel-cast process 2

1. Melt paraffin wax at 85c.
2. Print parts and stick into mold box
3. Spray in mold release
4. Pour in wax
5. Immediately put in vacuum chamber
6. Pull a -27mmHg vacuum
7. Wait 20 minutes under vacuum
8. Release vacuum and wait another 20 minutes
9. Stir in 0.5% citric acid as a dispersant
10. Mix in alumina to create a 50%?/vol solution
11. Mix in 5% white glue
12. Pour into mold.
13. Dry glue at 45c for 30 minutes.
14. Melt away paraffin at 70c
15. Remove from mold.
16. Sinter to 600c at 1c/min.
17. Sinter as hot as your kiln can manage (over 1300c is best) at 2c/min.

Gel-cast process 3

1. Melt paraffin wax at 85c.
2. Print parts and stick into mold box
3. Spray in mold release
4. Pour in wax
5. Immediately put in vacuum chamber
6. Pull a -27mmHg vacuum
7. Wait 20 minutes under vacuum
8. Release vacuum and wait another 20 minutes
9. Stir in 0.5% citric acid as a dispersant
10. Mix in alumina to create a 50%?/vol solution
11. Mix in 5% white glue
12. Pour into mold.
13. Dry glue at 45c for 30 minutes.
14. Melt away paraffin at 70c
15. Remove from mold.
16. Sinter to 600c at 1c/min.
17. Sinter as hot as your kiln can manage (over 1300c is best) at 2c/min.

Wax sucks. It’s waxy, it’s irritating, and it gets everywhere.

Gel-cast process 4

1. Print molds
2. Pour in 5% white glue alumina solution
3. Mix
4. Vacuum
5. Dry at 50c
6. Sinter.

This still leads to shrinkage.

This caused extreme porosity, presumably due to the stirring.

I’ve heard tell that Kiln elements are damaged by combustible atmospheres, which seems plausible - however, because we pre-melt the PLA, there’s only a bit of residue remaining on the green, so this shouldn’t be a problem.

Gel-cast process 5

1. Print a negative mold of your desired part out of PLA. Make a reservoir and sprue with at least 1 extra volume of material.
2. Add 1 volume of warm water to 1 volume of calcined alumina.
3. Mix gently by hand without introducing air.
4. Add 1.5% (by mass, of the entire solution) gelatine.
5. Mix again, avoiding foaming.
6. Dry at 50-60c for a few hours - the exact amount of time depends on the size of the part, and the allowable temperature depends on the geometry of the part to avoid cracking.
7. Transfer to an aluminum pan and bake at 100c for 20 minutes to drive off any remaining moisture.
8. Melt PLA mold at 300c on an aluminium foil pan. The green is quite delicate now, so be careful.
9. Refresh aluminum foil pan and melt again.
10. Sinter to 600c at 1c/min.
11. Sinter as hot as your kiln can manage (over 1300c is best) at 2c/min.

Tried firing at 450c to melt off PLA, cool, remove from first layer of aluminum, fire on aluminum again to 500c to burn off residue, then all the way to 1000c.

Ramp rate was very high; 20-30c/min, roughly.

Large PLA feedthroughs exploded violently near 500c. I think a slow ramp rate will be required.

Parts really can't be moved before firing - they just crumble.

Fired to 900c over the course of about an hour and a half. All the plastic was fired away; the parts looked amazing. However, they crumbled immediately. Clearly a higher firing temperature is required; probably the addition of a few percent clay is called for.

Going to try the same again, but with the addition of slip.

Tried 5% (2 grams) of slip.

Firing with 1 element at “low”.

160c - 1 hour 4 minutes

Part temp: 173c

192.2 - 1 hour 10 min.

At “low”, temperature stabilized at 215c.

“Medium” also ineffective. 1 element set to “High”. Oof, high is too much. Back to medium.

Called it at 360c. Opened the lid, one big part on stilts exploded, but everything else looks fine. One section caught fire immediately.

Now going to fire to 1000c.

Fired to 1050c. Parts had a little more structural integrity, but not much.

I think I know why - there’s only about 6% solids in the slip. I’m going to try a much higher percentage now.

Gel-cast process 6:

20 ml of slip + 20ml of alumina. Zero gelatine as a test.



# Wanna chat about this? Hit me up on twitter @0xDBFB7, or on irc.0xDBFB7.com:6667 #general.

[^operating]: Opening an operating kiln is extremely ill-advised: the thermal shock sent small chips of superheated refractory brick in all directions. Putting your arm into a 600 degree kiln in a crude attempt at brazing aluminum is not at all advisable. Putting your arm into said kiln while wearing a polyester jacket is positively insane. In unrelated news, I have a new jacket.