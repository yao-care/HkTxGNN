---
layout: default
title: Telmisartan
parent: 中證據等級 (L3-L4)
nav_order: 725
evidence_level: L3
indication_count: 5
---

# Telmisartan
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Telmisartan：從高血壓到腦動脈阻塞的探索性評估

## 一句話總結

Telmisartan 是 ARB（血管張力素受體阻斷劑）類藥物，臨床上廣泛用於高血壓治療。
TxGNN 模型針對此藥物提出 5 個高分預測適應症，其中僅有**腦動脈阻塞 (Cerebral Artery Occlusion)** 累積了實際證據——**3 個臨床試驗**與**17 篇文獻**（以動物模型為主），其餘 4 個候選（Prinzmetal angina、brain stem infarction、ABri amyloidosis、不明機轉肺高壓）目前**完全無臨床或文獻證據**，屬純模型外推。本報告以腦動脈阻塞為主軸深入評估，其餘候選僅列表供監測追蹤。

> ⚠️ 本藥物在香港**尚未上市**（0 張許可證），且**仿單警語／禁忌資料為阻斷性缺口（DG001）**，安全性初評尚無法進行。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（ARB 類藥物；香港無許可證文字紀錄可查證） |
| 預測新適應症（主軸） | 腦動脈阻塞 Cerebral Artery Occlusion |
| TxGNN 預測分數 | 99.95%（rank 1431） |
| 證據等級 | L3 |
| 決策階段 | S1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 五個預測適應症總覽（依 TxGNN 排序）

| 排序 | 疾病 | TxGNN 分數 | 臨床試驗 | 文獻 | 證據等級 | 建議 |
|------|------|-----------|---------|------|---------|------|
| 1 | Prinzmetal angina | 99.98% | 0 | 0 | L5 | Hold |
| 2 | Brain stem infarction | 99.98% | 0 | 0 | L5 | Hold |
| 3 | ABri amyloidosis | 99.97% | 0 | 0 | L5 | Hold |
| **4** | **Cerebral artery occlusion** | **99.95%** | **3** | **17** | **L3** | **Research Question** |
| 5 | Pulmonary HTN（不明多因子機轉） | 99.93% | 0 | 0 | L5 | Hold |

只有排序第 4 名的腦動脈阻塞具備可評估的實證基礎，以下章節針對此候選展開。

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 結構化的 MOA 條目（資料缺口 DG002），但根據多篇文獻與模型 rationale 描述，Telmisartan 是一款具**高脂溶性**的 ARB，透過阻斷 AT1 受體抑制 RAS（腎素-血管張力素系統），同時具有 **PPARγ 促效劑**活性，因此被稱為 "metabo-sartan"。

高血壓與腦動脈阻塞（缺血性腦中風）在病理上高度相關——高血壓本身就是腦中風的主要危險因子。多項動物 tMCAO（暫時性大腦中動脈阻塞）模型顯示，Telmisartan 除了降壓外，還能透過 PPARγ 活化減少氧化壓力（AGE、4-HNE）、抑制發炎介質（MCP-1、TNF-α、HMGB1）並縮小梗塞體積，顯示其可能具有超越降壓本身的**神經保護**效果。

人體端已有 Telmisartan 用於心血管事件（含中風）二級預防的大型 Phase 4 RCT（NCT01075698，N=1228，已完成）。然而，唯一直接鎖定「顱內疾病復發」的專屬試驗 TRIDENT（NCT03783754、NCT03785067）因入組嚴重不足（分別僅 4 人與 1 人）而提前終止，顯示從動物模型到人體驗證之間仍有明顯斷層。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | 已完成 | 1228 | 高風險高血壓患者使用 ARB（Telmisartan）vs 一般治療，觀察心血管事件（含中風）發生率與生物標記變化；非專門針對腦動脈阻塞的治療性試驗 |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA（MRI 子研究） | 已終止 | 4 | TRIDENT MRI 子研究，評估固定劑量三合一降壓藥於腦出血後患者；因入組不足終止 |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3（認知子研究） | 已終止 | 1 | TRIDENT 認知功能子研究，評估強化降壓對記憶衰退（CANTAB 量表）的影響；僅入組 1 人，統計效力不足 |

---

## 文獻證據

以下均為臨床前（動物）研究，多以大鼠 tMCAO 模型評估 Telmisartan 的神經保護效果：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | 動物研究 | J Stroke Cerebrovasc Dis | Telmisartan 減少 SHR-SR 大鼠 tMCAO 後的氧化壓力與 α-synuclein 堆積 |
| [25307428](https://pubmed.ncbi.nlm.nih.gov/25307428/) | 2014 | 動物研究 | J Stroke Cerebrovasc Dis | 長期改善 tMCAO 後大鼠代謝症候群相關分子（IR、PPAR-γ、AT1R） |
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | 動物研究 | J Neurotrauma | Telmisartan 縮小腦梗塞體積並降低梗塞周圍 cPLA2 表現 |
| [28699721](https://pubmed.ncbi.nlm.nih.gov/28699721/) | 2016 | 動物研究 | Indian J Exp Biol | Telmisartan 併用 nimodipine 於缺血前後給藥的神經保護比較 |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | 動物研究 | Pharmacol Biochem Behav | 非降壓劑量 Telmisartan + nimodipine 透過抑制腦細胞激素產生協同神經保護效果 |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | 動物研究 | Toxicology Reports | 透過 Nrf2/HO-1 路徑，Telmisartan 併用 ertugliflozin、omaveloxolone 減緩缺血再灌流神經毒性 |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | 動物研究 | PLoS ONE | Telmisartan 與 ramipril 頭對頭比較，於不同大鼠中風模型評估預防與神經保護效果 |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | 動物研究 | J Stroke Cerebrovasc Dis | Telmisartan 改善 SHR-SR 大鼠 tMCAO 後的發炎反應 |
| [18360031](https://pubmed.ncbi.nlm.nih.gov/18360031/) | 2008 | 動物研究 | Hypertens Res | 於動脈粥狀硬化 ApoE 缺失小鼠中，Telmisartan 減輕局部腦缺血 |
| [20498620](https://pubmed.ncbi.nlm.nih.gov/20498620/) | 2010 | 動物研究 | J Hypertens | 低劑量 Telmisartan 透過 PPAR-γ 活化預防糖尿病小鼠缺血性腦損傷 |

（另有 7 篇同主題文獻未列出，均為 tMCAO 動物模型的機轉延伸研究，可於需要時補充。）

---

## 香港上市資訊

Telmisartan 目前**未在香港取得任何藥品許可證**（`total_licenses = 0`），無法列出品名、劑型或核准適應症資料。

---

## 其他預測適應症（純模型預測，暫無實證，僅供監測）

| 疾病 | TxGNN 分數 | 機轉關聯簡述 |
|------|-----------|------------|
| Prinzmetal angina | 99.98% | 與冠狀動脈痙攣機轉關聯薄弱，ARB 藥理以降壓/RAS 抑制為主，無直接理論連結 |
| Brain stem infarction | 99.98% | 可能與一般缺血性腦中風的 RAS 調控假說類似，但此特定部位無任何實證支持 |
| ABri amyloidosis | 99.97% | 罕見體染色體顯性遺傳澱粉樣變性疾病，與 ARB 機轉無已知病理連結，判定為模型雜訊 |
| 不明多因子機轉肺高壓 | 99.93% | RAS 於部分肺高壓亞型可能有角色，但此分類缺乏明確病理靶點，無實證佐證 |

這 4 項建議**列入長期監測清單**，暫不投入研究資源。

---

## 安全性考量

香港許可證與仿單資料尚未收錄，**主要警語、禁忌症、藥物交互作用（DDI）皆為資料缺口**，其中仿單警語/禁忌屬**阻斷性（Blocking）缺口**，需先取得原廠仿單並解析後才能進行 S1 安全性初評。

> 安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 腦動脈阻塞方向雖有一致的臨床前機轉證據（多篇 tMCAO 動物研究）與一個支持性 Phase 4 RCT，但唯一直接鎖定此適應症的人體試驗（TRIDENT）因入組嚴重不足而**提前終止**，臨床證據尚未成熟（S1 / Research Question）。
- 其餘 4 個預測適應症完全無臨床或文獻證據，屬純模型外推，不建議現階段投入資源。
- 香港未上市、仿單安全性資料存在**阻斷性缺口（DG001）**，在此缺口補齊前無法進行任何安全性初評，故整體判定為 Hold。

**若要推進需要：**
- 取得 TFDA／原廠仿單，解析警語與禁忌症（DG001，阻斷性）
- 補齊 DrugBank MOA 結構化資料（DG002）
- 檢視是否有後續重啟或替代設計的 TRIDENT 類人體試驗
- 若考慮腦動脈阻塞方向，需規劃具足夠統計效力的前瞻性臨床試驗設計
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

