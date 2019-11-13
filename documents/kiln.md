#### The below is not worth reading

This project could be summarized as follows:

70/90% calcined Alumina to 30/10% Kaolin powder by weight, mix til homogeneous, add 4% by weight PVA white glue (wood glue, 45 to 70% solids). Do not breath dust; wear respirator.

Molding with pressure preferable to prevent voids. Dry for 3-5 hours at ambient. Machine at high rpm at 100 m/min surface, very low cutting force. Failed mold shots or mill tailings can be reconstituted with water and added to next batch. Process not ideal for production, see FAST/SPS.





![20190523_115341_HDR](../../ion_printer/media/20190523_115341_HDR.jpg)

### Sintering

#### Propane and oxy-acetylene sintering

<video src="../media/20181211_152721.mp4"></video>

> 

Very small parts ($<5  mm^3$) with simple geometries (component lead insulators, for instance) can be fired with nothing but a propane torch or Bunsen burner. There's a distinctive white glow that seems to indicate when the proper sinter temperature has been reached; I think this is due to the increased translucency of solid alumina compared to the powder form.

This is a very delicate, finicky procedure; once the binder has burned off, the green becomes very sensitive, and even the slight breeze from the torch can destroy it. The burnout must be performed "in-situ": moving the part from one oven to another invariably destroys it.

In addition, the radiative heat loss from larger parts prevents any level of sintering.

Obtaining reasonable strengths with any part larger than a few milimeters can require at least 10 minutes at temperature, as sinter quality depends not only on the peak temperature but rather on a non-linear temperature-time product.

If you're feeling really adventurous, you can try firing with an oxy-acetylene torch. 

<video src="../media/20181212_180113_cut.mp4"></video>

> Another failed lost-PLA gelatine test, this time with an oxy-acetalyne torch.



![20181212_182620_HDR](../media/20181212_182620_HDR.jpg)

> The best part produced by gas firing
>
> Note the green lines; these are tungsten oxide from the supporting wires.
>
> Note also the glassy, molten region in the center; the product of an unsteady hand holding a 3300c Acetylene torch.

<video src="../media/20181212_200256.mp4"></video>

> Digital strength measurements of the gas-fired parts

I can't recommend either of these methods. The slightest temperature gradient across the green body will make it shatter, which is difficult to prevent with local, uninsulated heating from burners.

![Screenshot from 2019-02-10 15-27-12](../media/Screenshot from 2019-02-10 15-27-12.png)

I've tried using graphite molds as a heat spreader to alleviate some of these issues, but it's not particularly effective; the differing coefficients of thermal expansion tend to crack the part, and the high emissivity of graphite prevents reaching the required temperatures, even with ludicrous heat input. 

A firebrick furnace to remove the radiative heat loss would probably work; but by that point I recommend building the kiln described below. 

### Vacuum furnace

I was hesitant to use my pristine high-vacuum system to burn glue.

### Conventional ceramics kilns

<video src="../media/20181111_162140.mp4"></video>

This surplus ceramics kiln ($50) draws 5.5 kilowatts while operating, reaching a peak temperature of 1250 C in 4 hours.

Most of the elements were broken upon receipt. Thin-gauge 220v 1-2 KW nichrome elements can be had for cents on eBay; while these were clearly not equivalent to the original heavy-gauge heaters, they performed satisfactorily.

As useful as these kilns may be for clays and porcelain firing, this ended up being poorly suited for technical ceramics purposes. The peak temperatures are insufficient for high-alumina parts, and the slow heating makes trial-and-error insufferable.

### Hot Surface Igniters to the rescue

Standard nichrome heating elements have a melting point proper of 1400c, yielding typical max furnace temperatures of ~1300c.

Unfortunately, those final few hundred degrees have a precipitous effect on the sintered strength of high-alumina mixes. 

Commercial kilns capable of above 1400c typically run for over \$3000, well over my budget. The kiln itself is relatively simple to build; however, commercial high-temp furnaces use SiC or MoSi2 elements, which typically cost ~\$300 each and are overkill for this application. An alternative element was sought. 

For the last few decades, gas central heating furnaces have used *hot surface igniters* to light the burners,  rather than a spark; apparently this yields a more reliable ignition. To reach the required ignition energies while surviving hourly cycles for decades, these use the same crystallized SiC as the commercial kilns.

The CoorsTek 271N (or Emerson 767A-372) SiC HSI ($33 CAD, Amazon) that was used for these tests was rated for a chilly 980 C at 102v to a positively balmy 1705 C at 132v (coorstek2017). The element drew a consistent 3.7A over the entire temperature range.

These have a reputation for being delicate; however, this one has been abused, quite throughly soiled by ceramic spall, and run continuously for hours without ill effect.

Recently, more physically resilient Silicon Nitride HSIs have been introduced, but these seem to be significantly less temperature resistant than the SiC versions and therefore poorly suited for this misuse. First, SiNi sublimates at 1800c, whereas SiC melts at some 2700c; but more critically, the SiNi elements invariably have Teflon wire insulation, rather than the fiberglass insulation found on SiC.

The SiNi HSIs also often specify an 80v DC supply, though haven't seen any discussion as to why that is.

These igniters are designed for intermittent use (cycles of 30 seconds or so); however, the SiC ones are built robustly, with a Steatite C220 (peak temperature 1700c) body and Nichrome 80 wires. Igniter body overheating does not seem to be a failure mode.

A shoddy muffle furnace was built to test these elements of the elements:



The furnace was made from a single standard Amaco 28035N 9" by 4-1/2" by 2-1/2"  firebrick ($15, Amazon). Construction couldn't be simpler:

- Cut in twain on a wet tile saw (cut like butter, and the moisture did not appear to affect the brick)

- Rend a 25mm slice from one half

- Drill a ~15mm deep pocket in the thin slice to accept the element body, along with a smaller hole for the element itself

  This was done to insulate the igniter body from the sweltering furnace cavity; however, I'm not sure that it was necessary

- Form the cavity in the other slice with the tile saw via judicious use of stops and fences

- Fix the element into place with fire-cement (*Imperial High-Temp Stove and Furnace Cement* was used, rated to 1460 C). Wait ~12 hours for the cement to dry, then slowly raise temperature over ~30 minutes.

A variac was used to raise the voltage a few percent over the 115v typical.

This kiln has performed beyond my wildest expectations. It heats to absurd temperatures ridiculously quickly; at 130v, it reaches 1000c in the first minute, and 1400c in the next, allowing for very rapid iterative testing. 

To risk stating the obvious, I've often observed that the time that each experiment cycle takes is a strong predictor for success in my crude, blunderbuss style of empirical research; if each new mystery is seperated by an interminable wait, it becomes difficult to maintain interest over years. 

<video src="../../ion_printer/media/20190518_135832.mp4"></video>

> First successful test
>
> +4% wood glue PVA binder and 70/30 Alumina/Kaolin, pressed with delrin "cookie-cutter" mold, 20 minute hold at 350C for binder burnout followed by a 10 minute pulse to >1500c
>
> Part was perfectly usable; in fact, it could barely be broken by hand
>
> One defect can be seen, which was traced to a void in the putty.

#### A curious case of degradation

After a particularly aggressive 40 minute 140v run, some very strange "bubbling" was noticed on the element.

![Screenshot from 2019-05-26 00-41-26](../../ion_printer/media/Screenshot from 2019-05-26 00-41-26.png)

![my_photo-bubble4](../../ion_printer/media/my_photo-bubble4.jpg)

If I understand @raj2015 correctly, this is quite a complex multi-stage phenomenon. 

First, the carbide oxidizes to silicon dioxide, which then reacts with the original carbide to form silicon oxide, evolving carbon monoxide gas in the interface layer. This inflates a bubble of the now-molten silicon dioxide layer. 

It's a very cool process, and I suppose the CO means you probably shouldn't run the kiln overnight in a bedroom.

The eroded cross section caused several hot spots, which will surely cause a thermal runaway:

![20190522_182607_HDR](../../ion_printer/media/20190522_182607_HDR.jpg)

At $25 per element, however, I'm not super concerned if it's destroyed in short order; I can probably make a hundred parts in this volume before it goes. 

#### Control

Previous concoctions using gelatin binders were quite sensitive to the temperature ramp; rates in excess of ~10 degrees per second would shatter the part. 

For this reason, a crude PID loop and an SSR were employed to bring the ramp and peak temperatures under closed-loop control. 

However, all of my thermocouples have now melted, and the PVA binder appears to be unconcerned by even the crazy dT/dts that this oven can hit at max power; so open-loop use is perfectly acceptable. 

I was initially concerned that the thermal shock of low-frequency SSR cycling would crack the brittle SiC (as with Peltier devices); however, these fears were completely unfounded.

![test_2](../../ion_printer/data/ceramics/test_2.png)

This run had a ~200c temperature offset due to the large thermal mass of the thermocouple and its placement in the kiln. Previous runs with other thermocouples generally demonstrated rates of 1000c/minute, with peak temperature in about 3 minutes.

<video src="../../ion_printer/media/20190514_165419.mp4"></video>

The PID coefficients depend on the thermocouple response, but 1,1,6 with windup limits of -300, 300 appears to be usable. 

This kiln is also useful for other purposes, like making toast in 2.4 seconds:

<video src="../../ion_printer/media/20190522_194150_cut.mp4"></video>





#### Tonsil 1:

