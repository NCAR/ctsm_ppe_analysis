import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

def rank_plot(da,nx,ax=None,sortby='delta'):
    df=pd.read_csv('cats.csv')
    x = top_n(da,nx,sortby=sortby)
    xdef = da.sel(param='default',minmax='min')

    if not ax:
        fig=plt.figure(figsize=[3,5])
        ax=fig.add_subplot()

    ax.plot([xdef,xdef],[0,nx-1],'k:',label='default')

    cats=[]
    colors=[]
    i=-1
    for xmin,xmax in x:
        i+=1
        c=df.color[df.param==xmin.param].values[0]
        cat=df.cat[df.param==xmin.param].values[0]
        if cat not in cats:
            cats.append(cat)
            colors.append(c)
        ax.plot([xmin,xmax],[i,i],color=c,lw=2)
        ax.plot(xmin,i,'o',color=c,fillstyle='none')
        ax.plot(xmax,i,'o',color=c)
    ax.set_yticks(range(nx))
    ax.set_yticklabels([p[:15] for p in x.param.values]);

    return colors,cats
    
def top_n(da,nx,sortby='delta'):
    ''' return top_n sorted by param effect or min-val or maxval '''
    flip={'max':1,'min':-1}
    if sortby=='delta':
        dx=abs(da.sel(minmax='max')-da.sel(minmax='min'))
    elif sortby=='max':
        dx=da.max(dim='minmax')
    elif sortby=='min':
        dx=-da.min(dim='minmax')
        
    if sortby=='none':
        ix=da.param!='default'
    else:
        ix=dx.argsort()[-nx:].values

    return da.isel(param=ix)