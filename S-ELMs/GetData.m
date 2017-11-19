function [P, T, TV] = GetData

    Sample=0.7*[1+j,1-j,-1+j,-1-j];
    S0=0.7*(-1-j);
    S00=0.7*(-1+j);
    
  %% Traning data
    S=[];
    S1=[];
    Y1=[];
    Y=[];
    temp=0;
    for a=1:1000
        num=0;
        num=fix(rand(1)*4)+1;
        S1(a)=Sample(num);
        if a==1
            O(a)=(0.34-j*0.27)*S1(a)+(0.87+j*0.43)*S0+(0.34-j*0.21)*S00;
        elseif a==2
            O(a)=(0.34-j*0.27)*S1(a)+(0.87+j*0.43)*S1(a-1)+(0.34-j*0.21)*S0;
        else
            O(a)=(0.34-j*0.27)*S1(a)+(0.87+j*0.43)*S1(a-1)+(0.34-j*0.21)*S1(a-2);
        end
        Y1(a)=O(a)+0.1*O(a)^2+0.05*O(a)^3+(normrnd(0,0.1)+j*normrnd(0,0.1));
        temp=a;
    end
    y1=Y1(3:temp);
    y2=Y1(2:temp-1);
    y3=Y1(1:temp-2);
    Y=[y1;y2;y3];
    S=S1(2:temp-1);
    P=Y;
    T=S.';
     
  %% Testing data  
    
    S=[];
    S1=[];
    Y1=[];
    Y=[];
    temp=0;
    for a=1:1000
        num=0;
        num=fix(rand(1)*4)+1;
        S1(a)=Sample(num);

        if a==1
            O(a)=(0.34-j*0.27)*S1(a)+(0.87+j*0.43)*S0+(0.34-j*0.21)*S00;
        elseif a==2
            O(a)=(0.34-j*0.27)*S1(a)+(0.87+j*0.43)*S1(a-1)+(0.34-j*0.21)*S0;
        else
            O(a)=(0.34-j*0.27)*S1(a)+(0.87+j*0.43)*S1(a-1)+(0.34-j*0.21)*S1(a-2);
        end        
        Y1(a)=O(a)+0.1*O(a)^2+0.05*O(a)^3+(normrnd(0,0.1)+j*normrnd(0,0.1));
        temp=a;
    end
    y1=Y1(3:temp);
    y2=Y1(2:temp-1);
    y3=Y1(1:temp-2);
    Y=[y1;y2;y3];
    S=S1(2:temp-1);
    
    TV.P=Y;
    TV.T=S.';




 