:slug: a-billion-stars-in-the-jupyter-notebook
:speaker: maarten-breddels
:year: 2017
:title: A billion stars in the Jupyter Notebook
:fulltitle: A billion stars in the Jupyter Notebook

This talk will show what is possible huge datasets that are becoming more prevalent in the era of big data. I will demonstrate this and the 3d visualization in the Jupyter notebook, the by now almost standard environment of (data) scientists.

With large astronomical catalogues containing more than a billion stars becoming common, we are preparing for methods to visualize and explore these large datasets. Data volumes of this size requires different visualization techniques, since scatter plots become too slow and meaningless due to overplotting. We solve the performance and visualization issue using binned statistics, e.g. histograms, density maps, and volume rendering in 3d. The calculation of statistics on N-dimensional grids is handled by Python library called vaex, which I will introduce. It can process at least a billion samples per second, to produce for instance the mean of a quantity on a regular grid. This statistics can be calculated for any mathematical expression on the data (numpy style) and can be on the full dataset or subsets, specified by queries/selections.

However, to visualize higher dimensional data in the notebook interactively, no proper solution existed. This led to the development of ipyvolume, which can render 3d volumes and up to a million glyphs (scatter plots and quiver) in the Jupyter notebook as a widget. With the browser as a platform, and the release of ipywidgets 6.0, these 3d plots can also be embedded in static html files and renders on nbviewer. This allows for sharing with colleagues, rendering on your tablet (paperless office), outreach, press release material, etc. Full screen stereo rendering allows for a virtual reality experience using your phone and Google Cardboard, a minor investment compared to other VR head mountables. Overlaying 3d quiver plots on a 3d volume rendering allows exploring a 6d (or higher) space. 

Vaex and ipyvolume can be used together to explore and visualize any large tabular data set, or separately to calculate statistics, and render 3d plots in the notebook and outside.
