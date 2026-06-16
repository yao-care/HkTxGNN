---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 240
evidence_level: L5
indication_count: 10
---

# Dipyridamole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dipyridamole：從心臟血管擴張劑到缺血性腦中風二級預防

## 一句話總結

Dipyridamole 是一種磷酸二酯酶（PDE）抑制劑及腺苷再攝取阻斷劑，全球已廣泛用於血小板功能抑制及心臟藥理壓力試驗。TxGNN 模型針對 10 項適應症進行預測，其中**缺血性腦中風 (Stroke Disorder)** 及**短暫性腦缺血發作 (TIA)** 的預測分數分別達 99.95% 及 99.87%，並有 **L1 等級**多項 Phase 3/4 RCT 及 Cochrane 系統評綜支持，建議 Proceed with Guardrails；TxGNN 排名第一的 Prinzmetal 心絞痛（99.99%）雖分數最高，但機轉分析顯示 dipyridamole 可能**誘發冠狀動脈痙攣**而非治療，屬潛在反適應症，維持 Hold。

---

## 所有預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| 1 | Prinzmetal 心絞痛 | 99.99% | L4 | ⚠️ Hold（機轉反適應症警示） |
| 2 | **缺血性腦中風** | **99.95%** | **L1** | **✅ Proceed with Guardrails** |
| 3 | 血栓性疾病 | 99.94% | L3 | 🔬 Research Question |
| 4 | 病竇症候群（體染色體顯性遺傳型） | 99.89% | L5 | ⚠️ Hold（機轉安全疑慮） |
| 5 | **短暫性腦缺血發作（TIA）** | **99.87%** | **L1** | **✅ Proceed with Guardrails** |
| 6 | 肌聚糖肌病 | 99.82% | L5 | Hold |
| 7 | Wildervanck 症候群 | 99.78% | L5 | Hold |
| 8 | 大頭畸形合併精神運動發育遲滯 | 99.77% | L5 | Hold |
| 9 | 外側靜脈竇血栓 | 99.72% | L4 | Hold |
| 10 | 海綿靜脈竇血栓 | 99.72% | L5 | Hold |

---

## 快速總覽（主要適應症）

| 項目 | 內容 |
|------|------|
| 藥物 | Dipyridamole (DB00975) |
| 原適應症 | 無香港許可證記錄（全球已核准用途：缺血性腦中風/TIA 二級預防、心臟藥理壓力試驗） |
| 最強證據適應症 | 缺血性腦中風 / TIA |
| TxGNN 預測分數（腦中風） | 99.95% |
| 證據等級 | L1（多項已完成 Phase 3/4 RCT） |
| 香港上市 | ✗ 未上市（0 張許可證） |
| 建議決策 | **Proceed with Guardrails**（腦中風/TIA） |

---

## 為什麼這個預測合理？

### 作用機轉

Dipyridamole 透過兩條互補路徑抑制血小板聚集：
1. **PDE 抑制**：阻斷血小板內磷酸二酯酶（尤其是 PDE3 和 PDE5），使 cAMP 及 cGMP 濃度升高，抑制血小板活化
2. **腺苷再攝取阻斷**：抑制 hENT1/hENT2 核苷轉運體，使細胞外腺苷濃度升高，透過 A2 受體進一步升高血小板內 cAMP

除抗血小板作用外，dipyridamole 還可放大內皮源性一氧化氮（NO）的血管保護效果，並具有抗氧化及抗炎特性，對血管內皮有多重保護機轉。

### 原適應症與預測新適應症的關聯性

缺血性腦中風及 TIA 的核心病理機轉為動脈粥樣硬化斑塊破裂、血小板活化聚集及血栓形成。Dipyridamole 的多重抗血小板和血管保護作用直接對應此病理過程，與 aspirin 的 COX-1 抑制機轉互補，形成協同作用。

ESPS-2（歐洲腦中風預防研究 2）首先確認 ER-dipyridamole + aspirin 組合（Aggrenox）較安慰劑顯著降低腦中風復發風險，ESPRIT 進一步確認其優於 aspirin 單藥（相對風險降低約 22%）。PRoFESS（n=20,332）雖顯示 Aggrenox 與 clopidogrel 療效相當，但確認了 dipyridamole 組合方案的安全性與非劣性。此組合已納入 AHA/ASA 及 ESO 腦中風指引作為 A 級推薦。

---

## 臨床試驗證據

### 缺血性腦中風（Stroke Disorder）核心試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | 完成 | 4,500 | **ESPRIT**：歐洲/澳洲可逆性缺血腦卒中預防試驗，直接比較 aspirin + dipyridamole vs aspirin 單藥，為本適應症核心 RCT，aspirin + dipyridamole 顯著優於 aspirin 單藥（A 級證據） |
| [NCT00153062](https://clinicaltrials.gov/study/NCT00153062) | Phase 4 | 完成 | 20,332 | **PRoFESS**：迄今最大規模腦中風二級預防 RCT，ER-dipyridamole + aspirin vs clopidogrel，確認兩組療效相當，dipyridamole 組合安全性獲驗證 |
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) | Phase 3 | 完成 | 1,295 | **JASAP**：日本 Aggrenox vs aspirin 81 mg 腦梗塞/TIA 復發預防，提供亞洲人群直接臨床數據（A 級） |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | 完成 | 551 | **EARLY**：比較 Aggrenox 在腦中風 24 小時內啟動 vs 7 日後啟動的安全性與療效，直接涉及 dipyridamole 啟動策略（B 級） |
| [NCT01661322](https://clinicaltrials.gov/study/NCT01661322) | Phase 3 | 終止 | 3,096 | 強化三重抗血小板（ACD）vs aspirin + dipyridamole（AD）高風險患者比較，Phase 3 但因安全疑慮提前終止（B 級，結論受限） |
| [NCT00238667](https://clinicaltrials.gov/study/NCT00238667) | Phase 3 | 完成 | 250 | **CADISS**：頸動脈剝離性腦中風，抗血小板 vs 抗凝血劑比較，dipyridamole 屬抗血小板選項（B 級，特定亞族群） |
| [NCT02630862](https://clinicaltrials.gov/study/NCT02630862) | NA | 完成 | 240 | 頸動脈血運重建患者抗血栓治療氧化壓力分析，評估 aspirin + dipyridamole 的抗氧化活性，義大利批准用於腦栓塞二級預防 |

### 短暫性腦缺血發作（TIA）直接相關試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00161070](https://clinicaltrials.gov/study/NCT00161070) | Phase 4 | 完成 | 4,500 | ESPRIT 明確納入 TIA 患者，為 TIA 後事件預防最直接大型 RCT（A 級） |
| [NCT00311402](https://clinicaltrials.gov/study/NCT00311402) | Phase 3 | 完成 | 1,295 | JASAP 納入腦梗塞/TIA 患者，亞洲人群直接數據（A 級） |
| [NCT00562588](https://clinicaltrials.gov/study/NCT00562588) | Phase 4 | 完成 | 551 | 涵蓋 TIA 患者的 Aggrenox 啟動時機試驗（B 級） |
| [NCT01613755](https://clinicaltrials.gov/study/NCT01613755) | Phase 4 | 完成 | 18 | Dipyridamole 對 metformin 藥動學影響，研究情境為 TIA/腦中風後合用糖尿病用藥，確認 dipyridamole 對 hENT4 轉運體的抑制 |

---

## 文獻證據

### 缺血性腦中風及 TIA（優先呈現 Tier 1 文獻）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11786451](https://pubmed.ncbi.nlm.nih.gov/11786451/) | 2002 | Meta-Analysis（Tier 1） | BMJ | **ATT 協作組**：高風險患者抗血小板治療大規模統合分析，確認抗血小板劑（包含 dipyridamole 組合）顯著降低死亡、心肌梗塞及腦中風複合終點 |
| [12535415](https://pubmed.ncbi.nlm.nih.gov/12535415/) | 2003 | Cochrane SR（Tier 1） | Cochrane Database | **Cochrane 系統評綜**：Dipyridamole 用於血管疾病患者腦中風及血管事件預防，ASA + dipyridamole 較 ASA 單藥提供額外 22% 風險降低 |
| [15569877](https://pubmed.ncbi.nlm.nih.gov/15569877/) | 2005 | Meta-Analysis（Tier 1） | Stroke | **個別患者資料 Meta-analysis**：整合多項 RCT 個別患者資料分析 dipyridamole 用於缺血性腦中風/TIA 二級預防，為本適應症最高等級證據 |
| [17636684](https://pubmed.ncbi.nlm.nih.gov/17636684/) | 2007 | Cochrane SR（Tier 1） | Cochrane Database | **Cochrane 更新版**：確認 ASA + dipyridamole 22% 相對風險降低，分析 ESPRIT 新數據後結論更為穩健 |
| [16625549](https://pubmed.ncbi.nlm.nih.gov/16625549/) | 2006 | Cochrane SR（Tier 1） | Cochrane Database | **Cochrane 中期更新**：與 2003/2007 版本呼應，持續確認 ASA + dipyridamole 療效 |
| [34399713](https://pubmed.ncbi.nlm.nih.gov/34399713/) | 2021 | Systematic Review（Tier 1） | BMC Neurology | 缺血性腦中風/TIA 二級預防抗血小板藥物網絡 meta-analysis，全面比較各抗血小板方案 |
| [8981292](https://pubmed.ncbi.nlm.nih.gov/8981292/) | 1996 | RCT（Tier 1） | J Neurol Sci | **ESPS-2**：歐洲腦中風預防研究 2，modified-release dipyridamole + ASA 首次大型 RCT，較安慰劑及單藥顯著降低腦中風復發 37% |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review（Tier 2） | Ann NY Acad Sci | Dipyridamole 在急性腦中風的抗血栓與神經保護作用探討，機轉回顧包含抗炎路徑 |
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Review（Tier 2） | ATVB | **Dipyridamole 轉譯醫學**：全面回顧 PDE 抑制、cAMP/cGMP 升高、抗血栓及血管保護機轉 |
| [30649687](https://pubmed.ncbi.nlm.nih.gov/30649687/) | 2019 | Clinical Study（Tier 2） | CNS Drugs | **台灣全國性研究**：dipyridamole + clopidogrel 用於 aspirin 不耐受的急性心肌梗塞後腦中風二級預防，提供亞洲人群真實世界數據 |

---

## ⚠️ 反適應症警示：Prinzmetal 心絞痛（TxGNN Rank 1）

儘管 TxGNN 給予本適應症最高預測分數（99.99%），機轉分析顯示存在潛在**加重病情風險**：

Dipyridamole 作為藥理性壓力試驗劑，其誘發的腺苷積累可觸發冠狀動脈痙攣。PMID [3421166](https://pubmed.ncbi.nlm.nih.gov/3421166/)（1988 年 Am J Cardiology）明確記載：dipyridamole 壓力試驗在變異型心絞痛患者中可作為 vasospasm 的觸發劑，需氨茶鹼（adenosine 拮抗劑）緊急終止。現有 15 篇相關文獻均在診斷/激發試驗脈絡下提及 dipyridamole，而非治療用途。此高分預測可能源於知識圖譜網路拓撲效應，**不建議作為 Prinzmetal 心絞痛治療推進**。

---

## 其他預測簡評

| 適應症 | 機轉評估 | Hold 原因 |
|--------|---------|---------|
| 病竇症候群 2 型（顯性遺傳型）| 腺苷抑制竇房結功能，可能加重緩脈症狀 | 安全疑慮，且無任何臨床/前臨床支持 |
| 肌聚糖肌病 | 肌聚糖複合體基因突變病理，與 dipyridamole 無已知機轉連結 | L5，純圖譜預測 |
| Wildervanck 症候群 | 先天性結構發育異常，無機轉連結 | L5，純圖譜預測 |
| 大頭畸形合併精神運動發育遲滯 | 神經發育遺傳疾病，無機轉連結 | L5，純圖譜預測 |
| 外側靜脈竇血栓 | 靜脈血栓病理首選抗凝血劑，抗血小板效益有限；唯一關聯試驗（透析患者鈣化研究）完全不相關 | L4 但機轉不適用 |
| 海綿靜脈竇血栓 | 感染性/靜脈血栓，需抗生素及抗凝血劑，抗血小板不適用 | L5，純圖譜預測 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

本 Evidence Pack 的 TFDA 警語、禁忌症及藥物交互作用資料均未取得（Data Gap DG001）。根據藥理知識，已知重要安全性注意事項包括：

- **頭痛**：最常見副作用，起因於血管擴張作用，常見於口服及靜脈劑型
- **低血壓**：靜脈注射（心臟壓力試驗劑量）時風險較高
- **腺苷相關禁忌**：支氣管痙攣患者（哮喘）及心臟傳導障礙患者（含病竇症候群）慎用
- **藥物交互作用**：
  - 腺苷（可顯著增強效果，需減量）
  - 茶鹼類藥物（可拮抗作用）
  - 合用抗凝血劑或其他抗血小板藥出血風險增加
  - 抑制 hENT4 轉運體，可能影響 metformin 吸收（PMID [NCT01613755](https://clinicaltrials.gov/study/NCT01613755) 的藥動學互動研究）

完整安全性資訊及香港特定警語需另行查閱原廠仿單及香港衛生署相關資料。

---

## 結論與下一步

**決策：Proceed with Guardrails（缺血性腦中風 / TIA 二級預防）**

**理由：**
ER-dipyridamole + aspirin（Aggrenox 組合製劑）在缺血性腦中風及 TIA 二級預防有最高等級（L1）臨床試驗支持，涵蓋 ESPRIT（n=4,500）、PRoFESS（n=20,332）、JASAP（n=1,295）等大型 Phase 3/4 RCT，並有 3 篇 Cochrane 系統評綜及個別患者資料 meta-analysis 佐證，已列入國際主要指引 A 級推薦；Dipyridamole 在香港目前無上市記錄，需評估藥品引進路徑。

**若要推進需要：**
1. **MOA 資料補全**：補齊 DrugBank 作用機轉詳細資料（Data Gap DG002）
2. **香港仿單安全資訊**：取得 TFDA/原廠仿單警語、禁忌症及完整 DDI 資料（Data Gap DG001）
3. **藥品引進評估**：評估 ER-dipyridamole + aspirin 組合製劑（如 Aggrenox）的香港藥劑業及毒藥管理局申請路徑
4. **亞洲族群特殊考量**：確認亞洲人群（特別是香港華人）的劑量調整及不良反應概況（JASAP 數據可作參考基礎）
5. **健保及醫院採購評估**：確認院所採購及醫療費用承擔可行性

**不建議推進之適應症：**
- ⚠️ Prinzmetal 心絞痛（機轉上可能誘發冠狀動脈痙攣，潛在反適應症）
- ⚠️ 病竇症候群（腺苷效應可能加重緩脈）
- ⚠️ 所有靜脈血栓疾病（外側/海綿靜脈竇血栓，需抗凝血劑而非抗血小板治療）

---

> **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後方可應用於臨床實務。預測結果由 TxGNN 模型生成，所有網站頁面及報告需包含 YMYL 免責聲明。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

