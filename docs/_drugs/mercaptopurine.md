---
layout: default
title: Mercaptopurine
parent: 高證據等級 (L1-L2)
nav_order: 402
evidence_level: L2
indication_count: 5
---

# Mercaptopurine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Mercaptopurine：從急性淋巴性白血病到骨髓性白血病 (Myeloid Leukemia)

## 一句話總結

Mercaptopurine（6-MP，硫嘌呤類似物）原本用於急性淋巴性白血病（ALL）與發炎性腸道疾病的免疫抑制/化療組合中。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，
目前有 **29 個相關臨床試驗**和 **20 篇文獻**支持這個方向（其中多數為 APL/AML 維持治療歷史實務證據）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴性白血病 (ALL)、發炎性腸道疾病（Crohn's disease、潰瘍性結腸炎）— 依證據包內文獻佐證 |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.94%（rank 1826） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 Mercaptopurine 詳細的作用機轉（MOA）正式資料。根據已知資訊，Mercaptopurine 是嘌呤類似物（thiopurine），經 HGPRT 路徑代謝後抑制 DNA/RNA 合成，對高增殖細胞（如白血病母細胞、活化淋巴球）具細胞毒性/免疫抑制作用，其療效已在急性淋巴性白血病與發炎性腸道疾病中被長期臨床實務證實。

急性淋巴性白血病與骨髓性白血病同屬造血系統惡性腫瘤，皆以抑制高增殖芽細胞為治療核心，機轉上具有相通性。事實上，證據包中的臨床試驗顯示，6-MP 早於 1960-1990 年代即作為急性骨髓性白血病（AML）誘導與維持化療的組合藥物（併用 cytarabine、daunorubicin），而急性前骨髓球性白血病（APL）的 PETHEMA、AIDA、AIDA2000 等經典方案，其維持治療階段更明訂納入「6-mercaptopurine + methotrexate + ATRA」的三藥組合，顯示此用法已有數十年的臨床實務基礎。近期（2022-2024）仍有 6-MP 併用 venetoclax 或 valproic acid 用於復發/難治 AML 的早期試驗持續進行，顯示其在骨髓性白血病治療領域尚未完全退場。

需注意的是，現代 AML 標準治療已逐漸轉向標靶藥物（如 venetoclax、FLT3/IDH 抑制劑），6-MP 目前多定位為維持治療或聯合用藥的輔助角色，而非一線核心藥物。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | 招募中 | 48 | 6-MP + valproic acid 併用治療不適合標準誘導治療之 AML/高風險 MDS 患者 |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | 招募中 | 10 | Venetoclax + 6-MP 治療復發/難治性 AML（ApoAML trial） |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | 完成 | 300 | PETHEMA LPA 2005：APL 以 ATRA+Idarubicin 誘導緩解，維持治療含 ATRA+MTX+6-MP |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | 完成 | N/A | AIDA 方案，緩解後以 ATRA+MTX+6-MP 作為分子/血液學復發之挽救治療 |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | 完成 | 105 | S0521：低/中風險 APL 維持治療 vs. 觀察之隨機試驗 |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | 未知 | 1068 | AIDA 協定，PCR 陰性患者以 ATRA/MTX/6-MP 間歇性維持治療 |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | 未知 | 80 | AIDA2000：風險分層治療 APL，兩年期 6-MP+MTX+ATRA 維持治療 |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | 完成 | 420 | 比較 tretinoin+化療±三氧化二砷鞏固治療後，以 tretinoin+6-MP+MTX 維持治療 APL |
| [NCT00700544](https://clinicaltrials.gov/study/NCT00700544) | Phase 3 | 完成 | 330 | GOELAMS SA-2002：老年 AML 緩解後輔以雄性素治療（背景試驗，非直接以 6-MP 為主要介入） |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | 完成 | 238 | 比較不同劑量 cytarabine 之多重化療方案於新診斷 AML/MDS |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92：於 DNR+BHAC+6-MP 誘導治療中加入 etoposide 並無額外效益 |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Cohort/Phase 2 | Cancer Investigation | 高劑量 6-MP + 中劑量 cytarabine 用於兒童 AML 首次緩解治療之可行性研究 |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | 不適合移植之 AML 患者以口服 6-MP+MTX 維持治療兩年 |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Cohort | Int J Hematol | Behenoyl cytarabine+DNR+6-MP 個別化誘導治療成人 AML，緩解率 71% |
| [8558199](https://pubmed.ncbi.nlm.nih.gov/8558199/) | 1996 | RCT | J Clin Oncol | 日本白血病研究群比較 BHAC 與 cytarabine ± ubenimex 之隨機試驗 |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemother Pharmacol | 全國性隨機試驗比較 daunorubicin 與 aclarubicin 併用 BHAC+6-MP+prednisolone |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | 臨床血液 | AML 與 APL 現行治療綜述 |
| [31983177](https://pubmed.ncbi.nlm.nih.gov/31983177/) | 2020 | RCT | Asian Pac J Cancer Prev | 節律性化療 vs. 緩和性 hydroxyurea 用於不適合強化治療之 AML 患者 |
| [8383541](https://pubmed.ncbi.nlm.nih.gov/8383541/) | 1993 | Case series | Ann Hematol | 微分化型 AML（AML-M0）5 例化療報告與文獻回顧 |
| [1657335](https://pubmed.ncbi.nlm.nih.gov/1657335/) | 1991 | Cohort | Zhonghua Yi Xue Za Zhi | Cytarabine+DNR+6-MP 併用治療成人 AML 之緩解誘導結果 |

---

## 細胞毒性

Mercaptopurine 屬於嘌呤類似物（thiopurine/purine analog）抗代謝藥物，長期作為血液惡性腫瘤化療組合藥物使用。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Antimetabolite / Purine analog，thiopurine 類） |
| 骨髓抑制風險 | 中至高度（證據包文獻提及 thiopurine 類藥物主要副作用包含骨髓抑制、胰臟炎、過敏反應、發燒） |
| 致吐性分級 | 低度 |
| 監測項目 | CBC（含白血球分類、血小板）、肝功能、TPMT/NUDT15 藥物基因體檢測（影響代謝與毒性風險） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

安全性資訊請參考原廠仿單（本評估未取得 TFDA/香港仿單警語與禁忌症資料，屬 Blocking 等級資料缺口，見下方結論）。

**⚠️ 重要安全性訊號（來自證據審查，非官方仿單資料）：**
證據包中對「Hodgkins lymphoma」的預測（rank 5）經審查後發現因果方向可能相反——多篇文獻（PMID 23094824、19767727、22031357、35501287 等）顯示 thiopurine 類藥物（azathioprine/6-MP）用於免疫抑制治療時，會**增加**淋巴瘤/淋巴增殖性疾病風險，屬藥物誘發之不良反應而非治療效益。此為知識圖譜嵌入相似性造成的疾病節點混淆（NHL vs. Hodgkin lymphoma），建議列為安全性監測重點，而非適應症擴充方向。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個 Phase 3/4 臨床試驗（PETHEMA、AIDA、AIDA2000、S0521）證實 6-MP 在急性前骨髓球性白血病（APL）維持治療中的長期實務角色，且有近期（2022-2024）Phase 1/2 試驗持續探索其於 AML/MDS 之新用法（併用 venetoclax、valproic acid），證據等級達 L2。
- 惟現代 AML 治療已轉向標靶藥物，6-MP 多屬輔助/維持角色而非一線治療，且香港目前**未上市**，需完整补齊法規與安全性資料才能進一步評估。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（目前為 Blocking 等級資料缺口 DG001）
- 取得 DrugBank 完整作用機轉（MOA）資料（High 等級資料缺口 DG002）
- 釐清「骨髓性白血病」是否指 AML 全體或特定亞型（如 APL），以精確評估適用族群
- 檢視 TPMT/NUDT15 基因型監測需求，以降低骨髓抑制風險
- 排除將 Hodgkin's lymphoma 預測誤用為適應症擴充方向，改列為安全性監測項目
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

