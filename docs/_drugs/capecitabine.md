---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine：從大腸直腸癌到多種胃癌亞型

## 一句話總結

Capecitabine（卡培他濱）是一種口服氟嘧啶前驅藥，在腫瘤組織中經胸腺嘧啶磷酸化酶（TP）轉化為 5-FU 發揮抗腫瘤作用，全球已核准用於大腸直腸癌及乳腺癌治療。
TxGNN 模型預測它可能對 **10 種胃癌亞型**有效，預測分數均達 99.89–99.94%；其中**胃管狀腺癌**（Gastric Tubular Adenocarcinoma）與**胃賁門腺癌**（Gastric Cardia Adenocarcinoma）各擁有多項已完成 Phase 3 RCT 支持，達 **L1 等級證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 大腸直腸癌、乳腺癌（全球核准；香港上市登記待核實） |
| 最佳預測新適應症 | 胃管狀腺癌 (Gastric Tubular Adenocarcinoma) |
| TxGNN 預測分數 | 99.94%（10 種胃癌亞型均達 99.89%+） |
| 最強證據等級 | L1（胃管狀腺癌、胃賁門腺癌） |
| 香港上市 | 待核實（登記資料不完整） |
| 許可證數 | 0 張（資料庫查詢結果，建議向衛生署確認） |
| 建議決策 | Proceed with Guardrails（針對 L1 亞型） |

---

## 所有預測適應症概覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----|--------|-----------|---------|------|
| 1 | Gastric Adenocarcinoma and Proximal Polyposis of the Stomach (GAPPS) | 99.94% | L5 | Hold |
| 2 | 印戒細胞胃腺癌 (Signet Ring Cell Gastric Adenocarcinoma) | 99.94% | L2 | Research Question |
| **3** | **胃管狀腺癌 (Gastric Tubular Adenocarcinoma)** | **99.94%** | **L1** | **Proceed with Guardrails** |
| 4 | 微浸潤期胃癌 (Microinvasive Gastric Cancer) | 99.94% | L5 | Hold |
| **5** | **胃賁門腺癌 (Gastric Cardia Adenocarcinoma)** | **99.91%** | **L1** | **Proceed with Guardrails** |
| 6 | 胃涎腺型癌 (Carcinoma of Stomach, Salivary Gland Type) | 99.91% | L3 | Research Question |
| 7 | 胃幽門癌 (Gastric Pylorus Carcinoma) | 99.91% | L4 | Hold |
| 8 | 胃體癌 (Gastric Body Carcinoma) | 99.90% | L2 | Proceed with Guardrails |
| 9 | EBV 相關胃癌 (EBV-associated Gastric Carcinoma) | 99.90% | L4 | Research Question |
| 10 | 惡性胃顆粒細胞瘤 (Malignant Gastric Granular Cell Tumor) | 99.89% | L5 | Hold |

---

## 為什麼這個預測合理？

Capecitabine 是一種設計用於腫瘤選擇性活化的前驅藥。口服吸收後，依序經羧基酯酶（CES）→ 胞嘧啶脫氨酶（CDA）→ 胸腺嘧啶磷酸化酶（TP）三步轉化為活性 5-FU。5-FU 抑制胸腺嘧啶合成酶（TS），阻斷腫瘤 DNA 合成。由於 TP 在多種實體腫瘤（尤其是胃腸道腺癌）中的表達量遠高於正常組織，卡培他濱在腫瘤局部的 5-FU 濃度顯著高於靜脈注射 5-FU，這正是其腫瘤選擇性的藥理基礎。

**胃管狀腺癌**為胃癌最常見組織學亞型（Lauren 分類腸型），TP 表達最豐富，對氟嘧啶類藥物敏感性最強。CLASSIC 試驗（PMID 22226517）確立 CAPOX（卡培他濱+奧沙利鉑）於 D2 胃切除術後輔助化療的金標準地位，其後 CheckMate 649、KEYNOTE-859、ORIENT-16、RATIONALE-305、RESOLVE、GLOW 等六項 Phase 3 大型試驗均以 CAPOX 作為化療骨幹，形成壓倒性的 L1 累積證據。**胃賁門腺癌**（Siewert Type II/III）則與胃管狀腺癌有相似的 TP 表達模式，NCT00040859（Phase 2，n=48）直接以 CAPOX 方案評估此解剖位置，NCT00374036（Phase 3，n=416）進一步提供最高等級錨點。

部分亞型的預測合理性明顯較低：印戒細胞癌（Lauren 瀰漫型）的 TP 表達可能低於腸型，多項回顧性資料顯示其對氟嘧啶類敏感性較差；微浸潤期胃癌的標準治療為內鏡切除（EMR/ESD），全身化療屬過度治療；惡性胃顆粒細胞瘤源自 Schwann 細胞（非上皮性），與腺癌具根本不同的腫瘤起源，TP 活化機轉在此不適用，TxGNN 高分可能為圖譜邊緣效應（graph leakage）所致。

---

## 臨床試驗證據

以下整合多個預測亞型中與卡培他濱直接相關的關鍵試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00374036](https://clinicaltrials.gov/study/NCT00374036) | Phase 3 | 完成 | 416 | 轉移或局部晚期胃/賁門腺癌化療策略比較，含卡培他濱方案臂，為本適應症最高等級試驗 |
| [NCT02494583](https://clinicaltrials.gov/study/NCT02494583) | Phase 3 | 完成 | 763 | 帕博利珠單抗 ± CAPOX 或 mFOLFOX6 一線治療晚期胃/GEJ 腺癌（KEYNOTE-059 前驅研究），卡培他濱為化療骨幹之一 |
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | 完成 | 48 | CAPOX 直接評估可測量轉移性食道/GEJ/胃賁門腺癌，卡培他濱為主要研究藥物（Grade A） |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | 完成 | 73 | 延伸新輔助治療局部晚期腺癌（食道/GEJ/胃賁門），含卡培他濱組 vs 5-FU 組隨機比較 |
| [NCT01295086](https://clinicaltrials.gov/study/NCT01295086) | 探索性 | 完成 | 27 | TEX（Taxotere + Eloxatin + Xeloda）+ Herceptin 一線治療 HER2+ 食胃腺癌，Xeloda 即卡培他濱 |
| [NCT02595424](https://clinicaltrials.gov/study/NCT02595424) | Phase 2 | 進行中（非招募） | 67 | 替莫唑胺 + 卡培他濱 vs 順鉑 + 依托泊苷，G3 非小細胞胃腸神經內分泌癌（卡培他濱為主要干預藥物，Grade A） |
| [NCT06238752](https://clinicaltrials.gov/study/NCT06238752) | Phase 2 | 完成 | 33 | 阿帕替尼 + 替雷利珠單抗 + CAPOX 一線治療含印戒細胞成分的晚期胃/GEJ 癌，評估聯合策略療效 |
| [NCT06121700](https://clinicaltrials.gov/study/NCT06121700) | Phase 2 | 招募中 | 55 | 放化療 + 抗 PD-1 後手術切除，寡轉移胃/GEJ 腺癌，含卡培他濱化療骨幹 |
| [NCT07091227](https://clinicaltrials.gov/study/NCT07091227) | Phase 2 | 尚未招募 | 66 | AK112 聯合含卡培他濱化療新輔助治療局部晚期含印戒細胞癌胃/GEJ 腺癌 |
| [NCT07000253](https://clinicaltrials.gov/study/NCT07000253) | Phase 2/3 | 尚未招募 | 290 | 寡轉移食道/胃癌一線治療後微創局部治療時機研究（OMEC-5），卡培他濱為標準骨幹化療成分 |

---

## 文獻證據

優先列出含卡培他濱方案的 RCT 及高影響力 Phase 3 試驗報告：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | RCT Phase 3 (CLASSIC) | Lancet | CAPOX 輔助化療顯著改善 D2 胃切除後 DFS（HR 0.56），確立 CAPOX 術後輔助化療金標準地位 |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | RCT Phase 3 (CheckMate 649) | Lancet | 納武利尤單抗 + 化療（CAPOX 為主要骨幹）一線治療 HER2- 胃/GEJ 腺癌，OS 顯著改善 |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | RCT Phase 3 (FLOT4) | Lancet | FLOT vs ECX/ECF（含卡培他濱的 ECX 臂）圍手術期化療，FLOT 優效，卡培他濱方案為對照標準 |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | RCT Phase 3 (RESOLVE) | Lancet Oncology | SOX vs CapOx D2 胃切除後輔助/圍手術期，CapOx 達非劣效性，確認卡培他濱可替代 S-1 |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | RCT Phase 3 (GLOW) | Nature Medicine | Zolbetuximab + CAPOX 一線治療 CLDN18.2+ HER2- 晚期胃/GEJ，卡培他濱為對照化療骨幹 |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | RCT Phase 3 (KEYNOTE-859) | Lancet Oncology | 帕博利珠單抗 + CAPOX 一線治療 HER2- 晚期胃/GEJ 腺癌，OS 顯著獲益（HR 0.78） |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | RCT Phase 3 (ORIENT-16) | JAMA | 信迪利單抗 + CAPOX 一線治療不可切除晚期胃/GEJ 癌，OS 顯著改善（HR 0.77） |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | RCT Phase 3 (RATIONALE-305) | BMJ | 替雷利珠單抗 + 化療（含 CAPOX 骨幹）一線治療晚期胃/GEJ 腺癌，OS 顯著改善 |
| [24175788](https://pubmed.ncbi.nlm.nih.gov/24175788/) | 2013 | RCT Phase 2-3 equivalent | Asian Pacific J Cancer | 卡培他濱直接對比 5-FU 用於胃腺癌術後放化療，療效相當，口服依從性更佳 |
| [29372626](https://pubmed.ncbi.nlm.nih.gov/29372626/) | 2018 | Phase 3 再分析 | Asia-Pacific J Clin Oncology | ML17032 試驗中國患者再分析：XP（Xeloda + 順鉑）非劣效於 FP（5-FU + 順鉑）一線治療晚期胃癌 |

---

## 香港上市資訊

根據本次查詢結果，Capecitabine 在香港的市場登記狀態為**未上市**，許可證數為 0。鑑於卡培他濱（Xeloda®，Roche）為全球廣泛使用的口服化療藥物，上述結果可能反映資料庫覆蓋範圍局限，而非藥物實際未於香港核准的狀態。

**建議向香港衛生署藥物辦公室（Pharmacy and Poisons Board of Hong Kong）核實 Capecitabine 的現行藥品登記情況。**

---

## 細胞毒性

Capecitabine 為氟嘧啶類抗腫瘤藥物，符合細胞毒性藥物管理要求：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類口服前驅藥） |
| 骨髓抑制風險 | 中度（嗜中性白血球減少、貧血、血小板減少；與 Oxaliplatin 合用時風險增加） |
| 致吐性分級 | 低至中度 |
| 特異性毒性 | 手足症候群（Hand-Foot Syndrome / PPE）為最具代表性毒性，發生率約 50–60%，重度者需停藥 |
| 監測項目 | CBC（含分類計數）、肝功能（AST/ALT/Bilirubin）、腎功能（eGFR；eGFR < 30 mL/min 禁用） |
| 處置防護 | 需依細胞毒性藥物處置規範操作（cytotoxic handling precautions）；口服劑型仍具污染風險 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 特別注意：Capecitabine 與 Warfarin（Coumadin）具有已知重要藥物交互作用，可顯著升高 INR 並增加出血風險，臨床使用時務必加強凝血功能監測。此資訊源自一般藥理知識，正式 DDI 數據需查閱 DrugBank 或原廠資料。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
胃管狀腺癌（L1）和胃賁門腺癌（L1）兩個亞型擁有多項已完成 Phase 3 RCT 的強力支持，卡培他濱在 CAPOX 方案中已是胃腺癌化療骨幹藥物；機轉明確（TP 依賴的腫瘤局部活化），在腸型胃腺癌中的生物學合理性極強。其他 8 個亞型則依證據強度分別列為 Research Question（印戒細胞癌、胃涎腺型癌、EBV 胃癌）或 Hold（GAPPS、微浸潤期、幽門癌、惡性顆粒細胞瘤）。

**若要推進需要：**
- 補充作用機轉詳細資料（查詢 DrugBank API，填補 MOA 空白）
- 向香港衛生署藥物辦公室核實 Capecitabine 的現行市場登記狀態，取得仿單原文
- 取得原廠仿單以確認警語、禁忌症及藥物交互作用（尤其 Warfarin、Phenytoin 的 DDI 風險）
- 針對印戒細胞癌（L2）補充 TP 表達量化研究，評估此亞型的實際療效預期
- EBV 陽性胃癌（L4）建議優先評估免疫治療策略（PD-L1/PD-L2 高表達），而非以氟嘧啶類化療為主軸
- 惡性胃顆粒細胞瘤（L5）及微浸潤期胃癌（L5）建議標注為 TxGNN 偽陽性候選，不納入後續研發優先序
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

