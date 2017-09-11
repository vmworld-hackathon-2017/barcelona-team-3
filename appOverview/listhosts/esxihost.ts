export interface IEsxiHost {
    hostId: number;
    hostName: string;
    hostDomain: string;
    hostMgmIp: string;
    hostMgmSm: string;
    hostMgmGw: string;
    hostMgmVlan: string;
    hostMgmMac: string;
    hostFirstNic: string;
    hostVmIp1: string;
    hostVmIp2: string;
    hostVmNm: string;
    hostVsIp: string;
    hostVsNm: string;
    hostNfsIp: string;
    hostNfsNm: string;
    hostIscsiIp1: string;
    hostIscsiIp2: string;
    hostIscsiNm: string;
    hostKb: string;
    hostFirstDisk: string;

}

export class EsxiHost implements IEsxiHost {
    constructor(public hostId: number,
        public hostName: string,
        public hostDomain: string,
        public hostMgmIp: string,
        public hostMgmSm: string,
        public hostMgmGw: string,
        public hostMgmVlan: string,
        public hostMgmMac: string,
        public hostFirstNic: string,
        public hostVmIp1: string,
        public hostVmIp2: string,
        public hostVmNm: string,
        public hostVsIp: string,
        public hostVsNm: string,
        public hostNfsIp: string,
        public hostNfsNm: string,
        public hostIscsiIp1: string,
        public hostIscsiIp2: string,
        public hostIscsiNm: string,
        public hostKb: string,
        public hostFirstDisk: string) {

    }
}