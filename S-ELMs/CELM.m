function CELM(name, PTGenerator)
% Sample: CELM('CELM', 'GetData')

fhandle = str2func(PTGenerator);
[I,T,TestData] = feval(fhandle); % read in training and testing data
% %%%%%%%%%%%%%%%%%%%%%%%%%%%
TestIn=TestData.P;
TestOut=TestData.T;

mkdir(name);
FileName = strcat(name,'\',name);
DirName = strcat(name,'\');

dim = size(I,1);
N = size(I,2);    % N: the number of training samples
N2 = 20;

cpu_time_Train_start=cputime;

weight = 0.1*(2*rand(N2,dim)-ones(N2,dim))+j*0.1*(2*rand(N2,dim)-ones(N2,dim));
bias = 0.1*rand(1,N2)+j*0.1*rand(1,N2);
ind=ones(1,N);
BiasMatrix=bias(ind,:);

tempH = (weight*I).'+ BiasMatrix;

H = asinh(tempH);
W = pinv(H)*T;

Train_time=cputime-cpu_time_Train_start;

rms_training=0;

tempH = (weight*I).'+ BiasMatrix;
H = asinh(tempH);
    
Yout = H*W;
E2 = T-Yout;    % training error
rms_training=sqrt(E2'*E2/N)  % rmse training

%%%%test%%%%
cpu_time_Test_start=cputime;

rms_testing=0;

num=size(TestIn,2);

ind=ones(1,num);
BiasMatrixT=bias(ind,:);

tempH_test = (weight*TestIn).'+ BiasMatrixT;
H_test = asinh(tempH_test);

YTest = H_test*W;
E3 = TestOut-YTest;    
rms_testing=sqrt(E3'*E3/size(TestIn, 2))

Test_time=cputime-cpu_time_Test_start;


save(FileName, 'H', 'Yout','W','weight','bias','T','I','YTest','Train_time','Test_time','TestIn','TestOut','rms_training','rms_testing');



