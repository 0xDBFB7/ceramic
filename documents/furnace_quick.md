---
title: 'Musings on an inexpensive 1500 C silicon carbide furnace'
link-citations: true
...

# Musings on an inexpensive 1500 C furnace

<!---

pandoc --filter pandoc-citeproc --bibliography=references.bib -s furnace_quick.md -o paper.html -H style.css
scp paper.html blog:/media/blog/src/furnace.html
scp -r images/furnace/ blog:/media/blog/src/images/

had to apt-cache clean to get back some space
-->

[Repository](https://github.com/0xDBFB7/ceramic/) | [References](https://htmlpreview.github.io/?https://github.com/0xDBFB7/ceramic/master/documents/references.html) | [Zotero](https://raw.githubusercontent.com/0xDBFB7/ceramic/master/documents/ceramics.rdf) | [BibTeX](https://raw.githubusercontent.com/0xDBFB7/ceramic/master/documents/references.bib)



![*Bake till golden brown, then turn over.*](images/furnace/20190518_142932_HDR.jpg){ width=40% }![](images/furnace/temperature-1559057994888.png){ width=40% }



A few years ago ago I was lucky enough to have some time to tinker with high-temperature ceramics. Very little of value was determined, primarily just empirical nonsense; I have not managed to figure out a consistent protocol for high-alumina parts. I figured I would quickly post the most useful fact in this document for the time being. I am certain that nothing here is even slightly novel.

Many of the Vacuum Hackers (among others) have much more expertise on ceramic blends, and you should probably talk to them instead.

<hr>

#### ~$40 "hot surface igniters", commonly used in gas furnaces for central heating, are a fantastic commodity source of pre-terminated silicon carbide heating elements. They appear to be usable to at least 1400 C continuously with 20 minute bursts to ~1600 C in air, and probably well over ~2000 C in inert gas or vacuum.

<hr>
#### Standard safety disclaimer:

 - At these temperatures, you can expect everything to be on fire. Wearing clothes that burn rather than melt is recommended, particularly when working with large commercial furnaces.
 - Parts with wet binders often explode on burnout, spraying superheated ceramic spall in all directions. A face shield is recommended.
 - Binder decomposition products can be quite noxious.
 - SiC elements are uninsulated and present an electrocution hazard (and also emit carbon monoxide, but that's hardly a risk).
 - Regularly working with aluminosilicate firebrick and fine alumina powders presents a risk of various pulmonary diseases and some (unsubstantiated) risk of neurological damage. Wear a respirator.
 - Some techniques discussed may involve the formation of titanium oxides, risking metal fume fever (see the case report of @Acute2008).

<hr>

It's relatively easy to get to 800 C or so with standard heating elements, microwave susceptors, or gas torches, sufficient for some low-fired >30% kaolin ceramic blends. With care in heating element support, termination, and insulation, commercial "high-fire" ceramics kilns can usually reach about 1300 C.

However, a very useful class of techniques practically demand a minimum of about 1400 C, including the most common high-purity oxide ceramics like $\text{Al}_2\text{O}_3$, $\text{MgO}$ and $\text{AlN}$, even if sinter-point-depressing additives are used (see awesome data from @Sintering1957a and @Vitreous1942). I believe this can be partly attributed to a change in regime from "liquid-phase" to diffusion-like "vapor-phase" sintering processes (@Sintering).

Furnaces that can reach such temperatures are usually quite expensive. Small zirconia sintering kilns are available, ostensibly for dental work, usually using MoSi2 heating elements, but these usually cost over $1500. There are a few sources of surplus high-temperature elements.

Acetylene torches do not appear to offer the required control over temperature ramp rate and produce strong thermal gradients that crack the green during burnout. Carbon-arc furnaces are pretty popular now but probably suffer from the same issues.

Some alternative techniques can often be used in specific circumstances, such as field-assisted sintering (@Fieldassisted2014, thanks @ice9). However, a general-purpose desktop furnace for small parts seemed like a pretty useful piece of equipment.

More critically, if a vacuum furnace is desired, standard Nichrome or Kanthal heater wire degrades very rapidly. See, for instance, this striking quote from @mazelsky1974multipurpose :

> The next factor investigated was the suitability of Kanthal A-1 as heater material. Although this material is suitable for use to 1325 C in air, at least one reference does not recommend its use in vacuum at temperatures over 1000°C. This warning is founded in the rapid evaporation of a component (chromium?) from the alloy and verified by tests we performed on bare wires in ultra-high vacuum. Sample filaments burned out after two hours or less at a surface temperature of 1200°C.

If a suitably high vacuum or inert atmosphere is available, sufficiently pure graphite or W, Ta or Mo boats can be made into acceptable heating elements, but it takes some effort to work around the low resistance of these materials.

![Sparkly!](images/furnace/hsi.JPG){ width=100% }

I recommend a `CoorsTek 271N` (equivalent to `Emerson 767A-372`) SiC HSI ($33 CAD pre-pandemic on Amazon) or equivalent with fiberglass wire insulation, Steatite C220 or Alumina body and nichrome wire. Beware elements with Teflon insulation. Both recrystallized SiC and SiN HSIs are available. The SiC elements are preferable due to the higher temperature resistance of SiC and a more rugged construction overall. SiN HSIs also often specify an 80v DC supply for reasons unknown.

SiC HSIs are mechanically delicate, but seem to tolerate ceramic spall and contamination relatively well.

Note that 220V elements seem to be quite rare: it appears to be hard to fabricate something with a sufficiently high resistance.

HSIs are apparently used because sparks do not provide the energy needed to ignite natural gas with perfect reliability over decades.

Getting above ~1500c involved increasing the 115V line voltage to about 135 V using a Variac. This does speed up element degradation a bit.

Of course, the element temperature must be higher than the furnace cavity; but they appeared to be sufficiently similar that I only report the temperature measured by thermocouple at the surface of the base.

### Degradation

I've consistently broken elements in idiotic ways before they burned out, so I have no data on lifespan; but you can probably expect on the order of a dozen hours at 1400 C in air.

Degradation occurs via a *fascinating* multi-step oxidation reaction described in detail by @Bubble2015 that evolves carbon monoxide and inflates large bubbles of $\text{SiO}_2$ mixed with SiC (if I'm understanding correctly - unlikely, given poor chemistry prowess!):

![](images/furnace/my_photo-bubble4.jpg){ width=100% }

Interestingly, a very similar "bubbling" failure mode was seen (@Oxidation2008 @NDE2010) on the reinforced-carbon-carbon panels on the leading edges of the space shuttle, which were coated with SiO and SiC for oxidation protection.

Such a carbon-carbide "conversion coating" seems to be relatively easy to perform in a furnace such as this one; see (@CARBIDE1957). SiC heating elements are also used on the ALQ-144 thermal missile jammer, so it's unlikely that my lab will be hit with a missile in the near future.


## Kiln 1

![](images/furnace/kiln.png){ width=100% }

This kiln was built using a single Amaco `28035N` 9" by 4-1/2" by 2-1/2" aluminosilicate firebrick ($15 pre-pandemic, Amazon) cut and pocketed using a wet tile saw (although a hacksaw would work fine); the element was then mounted with fire-cement (*Imperial High-Temp Stove and Furnace Cement*). The element was inserted through a slit in the firebrick to shield the terminals somewhat. Let cement dry overnight, then slowly raise temperature over course of ~30 minutes.

Fissures appear in the firebrick over the course of a few hours when running at 1500 C, but this doesn't seem to be a serious issue.

The alumina-foam firebrick is quite delicate, and the end-cap to which the element was mounted later broke during handling. Mounting with threaded rods and large washers is recommended.

I really like this furnace. It typically reaches 1000 C in one minute, and 1400 C in the next five to ten, allowing for very rapid iterative testing (useful for my crude, blunderbuss style of R&D). It can also toast bread in 2.4 seconds. Some green binders (gelatine, for instance) are sensitive to temperature ramp rate. PVAc seemed unfazed by these crazy dT/dts.

![Bread is not unfazed.](images/furnace/kiln2.png){ width=100% }

A PID control system can be added with an SSR: P: 1, I: 1, D: 2 to 6 based on thermocouple response, and integral windup limits of -300, 300 seems to be an acceptable starting point.

Typical ratings range from a tepid 980 C at 102v to a positively balmy 1705 C at 132v (@HighPerformance2017). Expect consistent 3.7A draw over entire temperature range.

![Flat-out temperature profile. Note that the MAX31855 thermocouple transducer stopped reading at about 1700 seconds and only recovered at 2200 seconds.](images/furnace/test_2.png){ width=100% }

Standard thin K-type thermocouple wire can operate briefly at 1400 C; McMaster-Carr's #3859K44 thermocouples survive a bit higher for a few minutes before being incinerated, though the high thermal mass leads to a ~200 C offset in this application (seen in the graph above).

Non-contact temperature measurement is more suitable, though all COTS bolometers begin to whimper at these temperatures.

The best option for temperature measurement is probably a **disappearing-filament pyrometer**. These are trivial to build.

If a Vis spectrometer is available, fitting the pleasant glow of the furnace to the Stefan-Boltzmann law can probably get you within a few hundred degrees.

A ratio pyrometer built from two photodiodes (or phototransistors, depending on your bias) with IR-cut and IR-pass filters may also work.

These techniques are complicated somewhat by alumina's selective radiation: the spectral emissivity curve looks like someone put overcooked pasta into Matplotlib. Worse still, it varies with temperature by about half an order of magnitude. I'm disappointed to find that 'spectral emissivity' has nothing to do with ghosts.


## Kiln 2 and speculation on next steps

 - Firebrick is crumbly and unlikeable.
 - Many interesting techniques require an inert or nitriding atmosphere.
 - In a rough vacuum, it should be possible to exceed 1,700 C continuously, probably limited only by the temperature at the nichrome termination.
 - It may be possible to measure the temperature in the kiln using the SiC element itself. The resistance didn't seem to change substantially as the element heated, but the bandgap might.

Most insulating materials that can withstand such temperatures are expensive or difficult to work with. Because of the $\text{P}\approx \text{T}^4$ nature of the Stefan-Boltzmann law vs the approximately linear dependence of conduction, at such high temperatures radiative insulation is the primary concern. For this reason, many concentric shells of multi-layer insulation may suffice.

The advantage here is that the efficiency of MLI depends only weakly on the emissivity and conductivity of the insulation. For this reason, a stack of machined graphite may be sufficient.

20 oz vacuum-insulated wine tumblers seem to make excellent chambers for this purpose.

![An overheated wine tumbler. ](images/furnace/wtf.JPG){ width=50% }


## Thanks for reading!

Suggest improvements on the GitHub issues page at <https://github.com/0xDBFB7/ceramic>, or hit me up \@0xDBFB7 on Twitter!

❤




#### Tonsil 0: Binders


'Gel-casting' is a technique where a slurry of ceramic powder mixed with a low-viscosity monomer or polymer (prototypically acrylamide, but now various others @Development1998) and crosslinker is injected into a mold, after which the crosslinker is triggered to form a solid green. This appears to be in vogue for ceramics production. Some advantages include very low binder percentages and correspondingly low green drying and firing shrinkage. Some effort was put into evaluating various gel-casting binders. (@Crosslinked2008)

However, aqueous gel-casting has a notable drawback in that most common binders tend to entrain water, meaning that even thin cross sections take many hours to properly dry. A solution of PEG can apparently be used to accelerate this drying @Drying2003 - I haven't tried this. The required crosslinking activators and are also usually difficult to obtain for the hobbyist.

(Note that, confusingly, both PVAc, poly(vinyl acetate), and PVOH, poly(vinyl alcohol), are each often referred to as 'PVA', despite having completely different properties. Standard white glues are an emulsion of primarily PVAc and some PVOH).

Alginates are a pretty neat tunable binder; the molecules cross-link together whenever a $\text{Ca}^{2+}$ or $\text{Mg}^{2+}$ ion is present in solution, meaning that the viscosity and trigger can be tuned with various chelators or ionic salts @Fabrication2003.

Glutinous rice flour @Study2014 is the strongest readily-available gel-casting binder that I'm aware of.

I have, however, had much better results from so-called low-pressure injection molding with a 15\% paraffin wax binder. Several suitable binders are discussed in @EVALUATION1965. A plastic syringe suffices for injection.

![](images/furnace/Screenshot from 2019-06-03 20-11-28.png){ width=50% }


#### Tonsil 1: Brazing

Alumina can be readily brazed using titanium @Sealing1957. This requires only a titanium interface layer; several fancy intermetallics are formed and the titanium adheres strongly to the alumina. The entire process must take place in a high vacuum or exceptionally clean argon atmosphere, else inert titanium oxides and nitrides will form.

A soft copper or Kovar interface layer is often used to prevent the differing thermal coefficients from cracking the ceramic when the weld cools.

See @Brazing1988 and @it2009 for details.

#### Tonsil 2: $\text{MnO}_2$

@Vitreous1942 describe how Manganese Dioxide can be used to depress the sinter point of pure alumina to more reasonable temperatures, sometimes without the use of silica. An impure, graphite-contaminated $\text{MnO}_2$ can be obtained from alkaline batteries; unfortunately, I have not yet been able to reproduce this effect.

The effects of sintering additives on the development of the crystalline structure are very interesting and counterintuitive (@Controlled1976 @Bulk2009). It would be interesting to see if these effects can be predicted with some accuracy by modern molecular dynamics procedures - something like DFT or Q ESPRESSO or HOOMD-Blue. I have done no research into this field - this is almost certainly already common practice.

#### Tonsil 3: Cataphoresis

A PVAc-bound alumina solution can be thinned considerably, and various objects can be dipped to form hard coatings. Attempts with graphite and aluminum have been successful; however, obtaining a uniform, tight-tolerance layer is somewhat difficult.

If such a layer is required, a variant of electrophoresis can be used; see @Electrophoretic1997 and @influence2004 for details. This technique is apparently often used to insulate indirectly heated cathodes.

#### Tonsil 4: Beta-alumina

Alumina can be found in two main allotropes: alpha-, and beta-. (and sapphire).

To my (surely flawed) understanding, the chief difference lies in the ionic conductivity, which allows for hermetic low-temperature anodic bonds to some materials using the esoteric Johnsen–Rahbek effect. See @FieldAssisted1979.

#### Tonsil 5: Foam

If a thin gelatine binder is used in a sol-gel, the solution can be beaten like egg white into a low density insulating foam. I don't know what this is useful for, but it's neat.

#### Tonsil 6: Fire

![](images/furnace/acetylene-1559058051640.png){ width=50% }

Attempts at acetylene sintering.

![Screenshot from 2019-02-10 15-27-45](images/furnace/Screenshot from 2019-02-10 15-27-45.png){ width=50% }

> Acetylene-sintered with 3% slip.


#### Tonsil 7: Lessons Learned

Perhaps it is useful to think about the test coupons that you use when optimizing processes. It seems like they should be as small, fast, and easy as possible while still reflecting the desired end product.

For instance, if you use an oversimplified test coupon, you might start overfitting your process to get good results on the coupon, rather than the final product you need. Don't overthink it though.

Perhaps there is some information in the design-of-experiments literature on this topic that may be of some use.

For some reason, the tests that I ran were largely sequential; run one mixture, observe the effects, modify the mixture slightly, etc. Parallelizing and pipelining may have made this go faster.



## Bibliography:
