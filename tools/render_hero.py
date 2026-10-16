# Hero renders for the portfolio: C13_V_ARA_FP, step THERM (-10 -> +40 C), deformation x30, |U| viridis 0-440 um
import os, sys, numpy as np, pyvista as pv
D='/mnt/user-data/uploads/2. Project Control/04_REPORTS/KRISS_2026/tools/out'; UD=os.path.join(D,'U_V_ARA_FP_THERM'); SF=30.0; CLIM=[0,440]
OUT=sys.argv[1]
pv.start_xvfb()
z=np.load(os.path.join(D,'surf_V_ARA_FP.npz')); S={}
for k in z.files:
    if k.endswith('__X'): n=k[:-3]; S[n]=dict(X=z[n+'__X'].astype(float),F=z[n+'__F'],L=z[n+'__L'])
def readU(name):
    lab=np.fromfile(os.path.join(UD,name+'.lab'),'<i4'); u=np.fromfile(os.path.join(UD,name+'.u'),'<f4').reshape(-1,3); return dict(zip(lab.tolist(),u))
def poly(X,F):
    c=[]
    for f in F:
        q=[i for i in f if i>=0]; c+=[len(q)]+q
    return pv.PolyData(np.asarray(X,float),np.asarray(c,np.int64))
M={}
for k,s in S.items():
    if k.startswith('Wall'): continue
    U=readU(k.upper() if not k.startswith('small') else k); u=np.array([U[l] for l in s['L']],float)
    m=poly(s['X']+SF*u,s['F']); m['U']=np.linalg.norm(u,axis=1)*1000; M[k]=m
outer=[k for k in M if k.startswith('enclosure') or k.startswith('Adhesive')]; inner=[k for k in M if k not in outer]
def render(keys,vec,zoom,name,win=(2000,1600)):
    p=pv.Plotter(off_screen=True,window_size=win); p.set_background('white')
    for k in keys:
        p.add_mesh(M[k],scalars='U',cmap='viridis',clim=CLIM,show_scalar_bar=False,ambient=0.28,diffuse=0.72,specular=0.15)
        fe=M[k].extract_feature_edges(feature_angle=35,boundary_edges=True,manifold_edges=False,non_manifold_edges=False)
        if fe.n_points: p.add_mesh(fe,color='#1b2a33',line_width=1.2)
    allm=pv.merge([M[k] for k in keys]); c=np.array(allm.center)
    p.camera.focal_point=c; p.camera.position=c+np.array(vec)/np.linalg.norm(vec)*allm.length*2.2; p.camera.up=(0,0,1); p.camera.view_angle=30
    p.reset_camera_clipping_range(); p.camera.zoom(zoom)
    img=p.screenshot(os.path.join(OUT,name),transparent_background=True,return_img=True); p.close(); print(name,img.shape)
render(outer,(-1.0,-1.25,1.75),1.25,'hero_outer.png')
render(inner,(-1.0,-1.25,1.10),1.3,'hero_inner.png')
