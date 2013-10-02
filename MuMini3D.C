#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include "TString.h"


void MuMini3D()
{
  
  vector<int> id_;
  int fid;
  ifstream infile;
  infile.open("data.dat");
  while(infile >> fid) {
    id_.push_back(fid);
  }
  
  gSystem->Load("libGeom");
  new TGeoManager("world","the simplest geometry");
  
  TGeoMaterial *mat = new TGeoMaterial("Vacuum",0,0,0);
  TGeoMedium   *med = new TGeoMedium("Vacuum",1,mat);
  TGeoVolume *top = gGeoManager->MakeBox("Top",med,5000.,5000.,5000.);
  gGeoManager->SetTopVolume(top);

  double scint_height  =  1.04;
  double scint_width   =  3.08;
  double scint_length  =  25.;
  double minigap       =  2.;
  double up_z_high     =  0.55*scint_height + 5.0;
  double down_z_high   = -0.55*scint_height + 5.0;
  double up_z_low      =  0.55*scint_height - 5.0;
  double down_z_low    = -0.55*scint_height - 5.0;
  
  unsigned int n_boxes = 32;
  TGeoVolume *boxes[32];
  
  for ( unsigned int boxid = 0; boxid < n_boxes; boxid++ ) {
    if ( boxid < 8 ) {
      boxes[boxid] = gGeoManager->MakeBox("box",med,scint_length,scint_height,scint_width);
      boxes[boxid]->SetLineColor(kWhite);
      top->AddNode(boxes[boxid],
		   boxid,
		   new TGeoTranslation(0,
				       (up_z_high*2),
				       -3.5*(scint_width*2)+(scint_width*2)*boxid));
    }
    else if ( boxid > 7 && boxid < 16 ) {
      boxes[boxid] = gGeoManager->MakeBox("box",med,scint_width,scint_height,scint_length);
      boxes[boxid]->SetLineColor(kWhite);
      top->AddNode(boxes[boxid],
     		   boxid,
		   new TGeoTranslation(-3.5*(scint_width*2)+(scint_width*2)*(boxid-8),
				       (down_z_high*2),
				       0));
    }
    else if ( boxid > 15 && boxid < 24 ) {
      boxes[boxid] = gGeoManager->MakeBox("box",med,scint_length,scint_height,scint_width);
      boxes[boxid]->SetLineColor(kWhite);    
      top->AddNode(boxes[boxid],
		   boxid,
		   new TGeoTranslation(0,
				       (2*up_z_low),
				       -3.5*(scint_width*2)+(scint_width*2)*(boxid-16)));
    }
    else if ( boxid > 23 && boxid < 32 ) {
      boxes[boxid] = gGeoManager->MakeBox("box",med,scint_width,scint_height,scint_length);
      boxes[boxid]->SetLineColor(kWhite);
      top->AddNode(boxes[boxid],
     		   boxid,
		   new TGeoTranslation(-3.5*(scint_width*2)+(scint_width*2)*(boxid-24),
				       (down_z_low*2),
				       0));
    }
  }
  
  for (int i = 0; i < id_.size(); i++) {
    boxes[id_[i]]->SetLineColor(kGreen);
  }
    
  gGeoManager->CloseGeometry();
  top->Draw("ogl");
  TGLViewer *v = (TGLViewer *)gPad->GetViewer3D();
  v->GetLightSet()->SetLight(TGLLightSet::kLightBottom, kFALSE);  
}
