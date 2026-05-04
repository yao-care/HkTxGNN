---
layout: default
title: Aliskiren
parent: 中證據等級 (L3-L4)
nav_order: 34
evidence_level: L3
indication_count: 7
---

# Aliskiren
{: .fs-9 }

證據等級: **L3** | 預測適應症: **7** 個
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

# Aliskiren：從高血壓到腦血管疾病

## 一句話總結

Aliskiren 是全球唯一獲臨床核准的直接腎素抑制劑，國際適應症為高血壓治療（香港/台灣目前均未上市）。
TxGNN 模型共預測 **7 個新適應症**，TxGNN 分數最高的是**肺動脈高壓（多因素機轉不明型）**（99.98%），但該預測目前無任何直接臨床證據。
在所有預測中，**腦血管疾病**（TxGNN 排名第 7，99.19%）擁有最豐富的臨床資料：**2 個臨床試驗**與 **13 篇文獻**，是目前最具研究推進潛力的方向（L3，Proceed with Guardrails）。

---

## 快速總覽（最高證據等級預測：腦血管疾病）

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（香港/台灣未上市；國際核准） |
| 預測新適應症 | 腦血管疾病 (Cerebrovascular Disorder) |
| TxGNN 預測分數 | 99.19% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 全部預測適應症一覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|--------|-----------|---------|------|
| 1 | 肺動脈高壓—多因素機轉不明型 | 99.98% | L5 | Hold |
| 2 | 肺動脈高壓—肺病/缺氧型 | 99.98% | L5 | Hold |
| 3 | 惡性高血壓性腎病 | 99.98% | L5 | Hold |
| 4 | 惡性腎血管性高血壓 | 99.98% | L4 | Research Question |
| 5 | Braddock 症候群 | 99.97% | L5 | Hold |
| 6 | 慢性肺心病 | 99.78% | L4 | Research Question |
| **7** | **腦血管疾病** | **99.19%** | **L3** | **Proceed with Guardrails** |

> **註**：TxGNN 高分反映知識圖譜的節點相似度，與臨床證據等級無必然關聯。排名第 1 的預測（L5）並非最具可行性；腦血管疾病（排名第 7）因有實際臨床研究支持，建議優先評估。

---

## 為什麼這個預測合理？

Aliskiren 是腎素-血管緊張素-醛固酮系統（RAAS）的最上游抑制劑，直接阻斷腎素（整個 RAAS 瀑布的限速酶）。與 ACE 抑制劑（ACEI）或血管緊張素受體阻斷劑（ARB）不同，Aliskiren 在訊號起點即截斷反應，理論上可完全消除下游血管收縮素 II（Angiotensin II）介導的血管收縮、氧化壓力及血管炎症。

在腦血管疾病方面，RAAS 系統扮演多重角色：調控腦部血流自動調節、促進動脈粥樣硬化形成、引發血管內皮功能障礙，以及在缺血性事件後誘導神經炎症。多項動物研究直接以 Aliskiren 介入缺血性中風和慢性腦缺血模型（PMID 21124781、21859961、27180190），均顯示神經保護效應。

然而，此方向存在重要的安全性悖論：ALTITUDE 臨床試驗（Aliskiren 加上 ACEI 或 ARB 用於第 2 型糖尿病患者）觀察到缺血性中風風險顯著上升（PMID 23418282）。此矛盾提示：Aliskiren 的腦保護潛力可能僅在特定情境下成立，且與合用藥物及基礎疾病密切相關。

> **目前缺乏詳細的作用機轉資料（MOA）**。建議補充 DrugBank DB09026 的完整機轉說明，以支撐機轉關聯性分析。

---

## 臨床試驗證據

### 腦血管疾病（排名第 7）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01417104](https://clinicaltrials.gov/study/NCT01417104) | Phase 2/3 | 提前終止 | 71 | ALPINE 試驗：評估 Aliskiren 對胸腹主動脈動脈粥樣硬化斑塊進展的影響（MRI 評估），與腦血管病高度相關。提前終止，樣本數遠低於預期，結論受限；終止原因需深入調查 |
| [NCT01454583](https://clinicaltrials.gov/study/NCT01454583) | N/A | 完成 | 15,337 | 德國 3A 登記研究：RAS 抑制劑（含 Aliskiren）治療高血壓的真實世界療效與安全性追蹤，涵蓋腦血管事件及腎功能不全等結果，提供大規模安全性參考資料 |

### 慢性肺心病（排名第 6）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | 完成 | 19 | P-DQIP 研究：藥師主導的初級照護處方安全性改善計畫（蘇格蘭），非 Aliskiren 特定藥物試驗，與慢性肺心病的直接相關性極低，僅供參考 |

---

## 文獻證據

### 腦血管疾病（排名第 7）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40013543](https://pubmed.ncbi.nlm.nih.gov/40013543/) | 2025 | Cochrane 系統回顧 | Cochrane Database Syst Rev | 腎素抑制劑 vs ARBs 治療原發性高血壓：降壓幅度相當，整體耐受性良好 |
| [37439548](https://pubmed.ncbi.nlm.nih.gov/37439548/) | 2023 | Cochrane 系統回顧 | Cochrane Database Syst Rev | 一線利尿劑 vs 其他降壓藥類別的死亡率與病率比較 |
| [26523993](https://pubmed.ncbi.nlm.nih.gov/26523993/) | 2015 | 臨床試驗分析 | Atherosclerosis | AQUARIUS 試驗分析：Aliskiren 對有/無糖尿病冠心病患者的冠狀動脈粥樣硬化進展及主要不良心血管事件的影響 |
| [23418282](https://pubmed.ncbi.nlm.nih.gov/23418282/) | 2013 | 臨床安全性分析 | J Renin Angiotensin Aldosterone Syst | ⚠️ **安全警訊**：ALTITUDE 試驗中 Aliskiren 與低血壓及缺血性中風風險增加相關，推測機轉為 Bezold-Jarisch 反射致交感神經撤退及低血壓 |
| [23541659](https://pubmed.ncbi.nlm.nih.gov/23541659/) | 2013 | Meta 分析/回顧 | Can J Cardiology | Aliskiren 與 RAS 抑制劑合用的安全性再評估：提醒臨床謹慎，但部分族群可能仍有效益 |
| [21859961](https://pubmed.ncbi.nlm.nih.gov/21859961/) | 2011 | 動物研究 | Hypertension | Aliskiren 顯著減輕小鼠慢性腦缺血（雙側頸動脈狹窄）所致腦損傷與認知障礙，獨立於降壓效應 |
| [21124781](https://pubmed.ncbi.nlm.nih.gov/21124781/) | 2010 | 動物研究 | PLoS One | 首次證實 Aliskiren 在表現人類腎素/血管緊張素元基因鼠的中風模型中具神經保護效應，類似 ARB 預處理的效果 |
| [27180190](https://pubmed.ncbi.nlm.nih.gov/27180190/) | 2016 | 動物研究 | Neurochem Res | Aliskiren 在小鼠缺血性中風（tMCAO）模型中上調 p-PI3K、p-AKT、Bcl-2 表達，發揮抗凋亡腦保護作用 |
| [26188211](https://pubmed.ncbi.nlm.nih.gov/26188211/) | 2015 | 臨床試驗子分析 | Eur Heart J | ALTITUDE 試驗：第 2 型糖尿病患者發生心血管及腎臟事件後的死亡風險分析 |
| [25131447](https://pubmed.ncbi.nlm.nih.gov/25131447/) | 2014 | 基礎研究 | Neurobiology of Disease | 腦幹 RAAS 與 MCP-1 的交互作用調控缺血性中風後升壓反應機轉，Aliskiren 介入顯示保護效益 |

### 惡性腎血管性高血壓（排名第 4）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17485026](https://pubmed.ncbi.nlm.nih.gov/17485026/) | 2007 | 回顧/機轉分析 | Am J Hypertension | 6 個臨床試驗（>5,000 患者）：Aliskiren 降壓效果與 ACEI/ARB 相當；提出高腎素狀態下「反應性腎素分泌」的反饋限制問題，對惡性腎血管性高血壓具特殊參考價值 |

### 惡性高血壓性腎病（排名第 3）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37919077](https://pubmed.ncbi.nlm.nih.gov/37919077/) | 2023 | 基礎研究 | Front Biosci Landmark Ed | 腎素依賴性高血壓中，腎素裂解 C3 形成 C3a，透過 C3aR 訊號誘發腎小管間質纖維化；RAAS 抑制（包含腎素抑制）在此模型中具腎保護潛力 |

### 慢性肺心病（排名第 6）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17890152](https://pubmed.ncbi.nlm.nih.gov/17890152/) | 2007 | 臨床試驗更新/回顧 | Eur J Heart Failure | ESC 2007 試驗更新，包含 ALOFT 試驗（Aliskiren 用於心衰患者）初步結果報告，心衰與慢性肺心病有病理重疊 |
| [39210725](https://pubmed.ncbi.nlm.nih.gov/39210725/) | 2024 | 事後分析 | JAMA Cardiology | PARADIGM-HF 及 PARAGON-HF 事後分析：Sacubitril/valsartan 對心衰全因住院的影響，提供 RAAS 抑制在心衰相關疾病的背景參照 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **⚠️ 重要臨床警訊（來自文獻）**：ALTITUDE 試驗（PMID 23418282, 26188211）顯示，Aliskiren 與 ACEI 或 ARB **合用**於第 2 型糖尿病患者時，與缺血性中風風險增加及低血壓相關。此發現已促使美國 FDA 發出警告，禁止上述合用方案。在腦血管疾病老藥新用研究設計時，**必須明確排除此高風險情境**（糖尿病患者合用 RAAS 雙重阻斷），並設定嚴格的入組排除標準。

---

## 結論與下一步

### 各適應症決策摘要

| 適應症 | 決策 | 理由 |
|--------|------|------|
| 肺動脈高壓—多因素機轉不明型 | **Hold** | L5：TxGNN 高分但零臨床/文獻證據；「機轉不明」亞型本身的 RAAS 貢獻高度不確定 |
| 肺動脈高壓—肺病/缺氧型 | **Hold** | L5：相關文獻均為缺氧一般機轉研究，無 Aliskiren 特定證據 |
| 惡性高血壓性腎病 | **Hold** | L5：機轉合理，但僅有間接基礎研究，無臨床資料支持 |
| 惡性腎血管性高血壓 | **Research Question** | L4：高腎素狀態與直接腎素抑制機轉高度契合；需注意反應性腎素分泌的反饋效應 |
| Braddock 症候群 | **Hold** | L5：罕見先天性基因疾病，與 RAAS 無已知分子連結；預測可能為圖譜偏差 |
| 慢性肺心病 | **Research Question** | L4：與心衰病理有部分重疊，ALOFT 試驗提供間接佐證，但直接外推仍需謹慎 |
| **腦血管疾病** | **Proceed with Guardrails** | L3：動物實驗顯示神經保護效應；大型登記研究提供安全性資料；機轉基礎充分 |

---

**決策：腦血管疾病方向 — Proceed with Guardrails**

**理由：**
Aliskiren 的腎素抑制機轉與腦血管疾病的病理生理（血管炎症、動脈粥樣硬化、腦缺血）有合理的機轉連結，並有多項動物研究及一個真實世界大型登記研究支持其安全性。然而，ALTITUDE 試驗揭示的安全性悖論（糖尿病患者中風風險增加）需作為重要守護條件，任何後續研究必須嚴格控制合用藥物與適用族群。

**若要推進腦血管疾病方向，需要：**
1. **釐清 ALPINE 試驗（NCT01417104）提前終止原因**：確認是否因安全性、資金或療效不足
2. **補充 Aliskiren 完整 MOA 資料**（DrugBank DB09026）：加強機轉關聯性論證
3. **設計排除高風險族群的研究方案**：明確排除第 2 型糖尿病患者合用 ACEI/ARB 的情境
4. **優先以單獨給藥（非雙重 RAAS 阻斷）設計**臨床試驗或觀察性研究
5. **建立台灣/香港上市可行性評估**：目前香港無許可證，若有潛在研究需求，需評估重新申請或研究用藥特例的可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

