---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 854
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Telmisartan：預測新適應症為腦動脈阻塞 (Cerebral Artery Occlusion)（證據等級 L5）。原適應症：高血壓、中風、腦血管疾病、腦梗塞"
monitor_inn: "TELMISARTAN"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis"]
---

# Telmisartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Telmisartan：從高血壓與腦血管疾病到腦動脈阻塞

## 一句話總結

Telmisartan 是一種血管收縮素 II 受體阻斷劑（ARB），原本用於高血壓與腦中風相關疾病。
TxGNN 模型預測它可能對**腦動脈阻塞 (Cerebral Artery Occlusion)** 有效，
目前有 **3 個臨床試驗**（皆為間接或無法解讀的證據）和 **18 篇文獻**（皆為前臨床動物研究）支持這個方向。

> 說明：TxGNN 預測分數最高的是 Prinzmetal 心絞痛（99.98%），但該項目沒有任何試驗或文獻。本報告以證據最多的「腦動脈阻塞」作為主要評估對象，其餘預測列於「快速總覽」之後的補充。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、中風、腦血管疾病、腦梗塞（來自知識圖譜；香港許可證資料中未載明核准適應症文字） |
| 預測新適應症 | 腦動脈阻塞 (Cerebral Artery Occlusion) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L4（前臨床研究與機轉研究；無已完成的 Phase 3 RCT 支持此適應症） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題，待人體證據） |

### 其他預測適應症（皆僅有模型預測，證據等級 L5）

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 1 | Prinzmetal 心絞痛 | 99.98% | 無試驗與文獻；可能與血管擴張和內皮保護作用有關 |
| 2 | 腦幹梗塞 | 99.98% | 與原有中風適應症相近，但無部位特異性證據 |
| 3 | ABri 類澱粉變性 | 99.97% | 罕見疾病，僅有間接的類澱粉相關前臨床線索 |
| 5 | 機轉不明的多因素肺高壓 | 99.93% | 無證據；全身性降壓作用在肺高壓患者可能是安全疑慮 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Telmisartan 是 AT1 受體阻斷劑，同時具有部分 PPAR-γ 促效作用（文獻中稱為「metabosartan」）。這些特性使它除了降血壓之外，還可能改善代謝、減少發炎與氧化壓力。

腦動脈阻塞是缺血性中風的直接成因，與 Telmisartan 已知的中風、腦梗塞適應症高度重疊。文獻中的動物實驗顯示，在大腦中動脈阻塞（MCAO）模型中，Telmisartan 可縮小梗塞體積、降低氧化壓力與神經發炎，並與 nimodipine 產生協同神經保護作用。部分研究指出這與 PPAR-γ 活化及 Egr-1 抑制有關。

不過，這些證據全部來自動物或實驗模型。人體試驗方面，Phase 4 試驗是心血管疾病預防研究，兩個 TRIDENT 子試驗則因收案極少而提前終止，因此目前無法證實對腦動脈阻塞的臨床療效。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01075698](https://clinicaltrials.gov/study/NCT01075698) | Phase 4 | 完成 | 1228 | 以 Telmisartan 對比一般治療，用於高風險高血壓患者的心血管疾病預防；屬間接證據，未以腦動脈阻塞為終點 |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | 終止 | 4 | TRIDENT MRI 子研究（三合一降壓藥用於腦出血後預防）；僅收 4 人，無法判讀療效，且無法分離 Telmisartan 的貢獻 |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | 終止 | 1 | TRIDENT 認知子研究（三合一降壓藥與記憶衰退）；僅收 1 人，無可用療效資料 |

---

## 文獻證據

以下文獻皆為前臨床（動物或實驗）研究，未發現人體 RCT。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19604102](https://pubmed.ncbi.nlm.nih.gov/19604102/) | 2009 | 動物研究 | J Neurotrauma | 大鼠 MCAO 模型中，Telmisartan 縮小腦梗塞體積並降低梗塞周邊 cPLA2 |
| [24780412](https://pubmed.ncbi.nlm.nih.gov/24780412/) | 2014 | 動物研究 | J Stroke Cerebrovasc Dis | 降低 SHR-SR 大鼠 tMCAO 後的氧化壓力與磷酸化 α-synuclein 堆積 |
| [25307428](https://pubmed.ncbi.nlm.nih.gov/25307428/) | 2014 | 動物研究 | J Stroke Cerebrovasc Dis | 長期改善 tMCAO 後代謝症候群相關分子（IR、PPAR-γ、AT1R） |
| [25245484](https://pubmed.ncbi.nlm.nih.gov/25245484/) | 2014 | 動物研究 | J Stroke Cerebrovasc Dis | 減輕 tMCAO 後腦部發炎反應 |
| [24650592](https://pubmed.ncbi.nlm.nih.gov/24650592/) | 2014 | 動物研究 | Pharmacol Biochem Behav | 非降壓劑量的 Telmisartan 與 nimodipine 產生協同神經保護，並降低腦細胞激素 |
| [21901125](https://pubmed.ncbi.nlm.nih.gov/21901125/) | 2011 | 動物研究 | PLoS One | 比較 Telmisartan、ramipril 及其合併用於大鼠中風預防與急性缺血神經保護 |
| [28699721](https://pubmed.ncbi.nlm.nih.gov/28699721/) | 2016 | 動物研究 | Indian J Exp Biol | 比較缺血前與缺血後給予 Telmisartan 與 nimodipine 合併的神經保護效果 |
| [41341617](https://pubmed.ncbi.nlm.nih.gov/41341617/) | 2025 | 動物研究 | Toxicol Rep | 透過 Nrf2/HO-1 路徑減輕腦缺血再灌流引起的神經毒性 |
| [24435631](https://pubmed.ncbi.nlm.nih.gov/24435631/) | 2015 | 動物研究 | Transl Stroke Res | 長期評估 Telmisartan 對 tMCAO 後 Alzheimer 類澱粉生成的影響 |
| [32992165](https://pubmed.ncbi.nlm.nih.gov/32992165/) | 2020 | 動物研究 | J Stroke Cerebrovasc Dis | PPARγ 活化抑制 Egr-1，對缺血性腦損傷具保護作用 |

（另有 8 篇相關動物研究未列於此表。）

---

## 香港上市資訊

香港共有 20 張有效的單方許可證，皆為錠劑。資料中未載明劑型與核准適應症文字，以下列出主要 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45841 | MICARDIS TAB 40MG | 錠劑 | 資料未載明 |
| HK-45842 | MICARDIS TAB 80MG | 錠劑 | 資料未載明 |
| HK-61881 | TELMISARTAN SANDOZ TABLETS 40MG | 錠劑 | 資料未載明 |
| HK-63207 | TELMOTENS TABLETS 40MG | 錠劑 | 資料未載明 |
| HK-66969 | MICAVID TABLETS 40MG | 錠劑 | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**（非仿單內容）：肝衰竭、腎臟疾病、無尿症、膽汁鬱積、胰臟炎、膽囊疾病、全身性紅斑性狼瘡、低血鉀、糖尿病（含酮酸中毒）、痛風與高尿酸血症、高血鈣、副甲狀腺機能亢進、低血壓、腎動脈阻塞等。
- **藥物交互作用**：共查得 100 筆，其中較需注意的：
  - **嚴重（Major）**：檸檬酸鉀 (Potassium citrate)、碳酸氫鉀 (Potassium bicarbonate)，有高血鉀風險
  - **中度（Moderate）**：皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）、Acetylsalicylic acid、Bupropion、Morphine、SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin）、Exenatide、胰島素等
- 此外，若用於肺高壓等特殊族群，需留意全身性降壓作用。

仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（腦動脈阻塞列為研究問題）**

**理由：**
- Telmisartan 在動物模型中有一致的神經保護訊號，機轉上合理，且與已核准的中風適應症相近。但人體證據僅有間接的 Phase 4 心血管預防試驗，以及兩個因收案極少而無法判讀的終止試驗，不足以支持推進。
- 其他預測適應症（Prinzmetal 心絞痛、腦幹梗塞、ABri 類澱粉變性、肺高壓）僅有模型分數，無任何實證，維持 Hold。

**若要推進需要：**
- 取得 Telmisartan 的作用機轉資料（MOA）與香港仿單的警語、禁忌症
- 針對腦動脈阻塞／缺血性中風設計或尋找直接的人體試驗（如 Telmisartan 單方的 RCT 或對既有中風預防試驗的次族群分析）
- 評估神經保護所需劑量與降壓劑量的差異，以及急性期給藥的血壓安全性
- 若考慮肺高壓，需先評估全身性降壓作用的安全風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

