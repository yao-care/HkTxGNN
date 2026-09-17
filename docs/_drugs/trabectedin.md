---
layout: default
title: Trabectedin
parent: 高證據等級 (L1-L2)
nav_order: 760
evidence_level: L2
indication_count: 1
---

# Trabectedin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Trabectedin：從肉瘤／卵巢癌到乳癌

## 一句話總結

Trabectedin 是一種海洋來源的細胞毒性抗腫瘤藥物，文獻顯示其在歐盟已核准用於**軟組織肉瘤**二線治療及與 PEG 化微脂體 doxorubicin 併用治療**卵巢癌**（香港無正式許可證資料）。
TxGNN 模型預測它可能對**乳癌 (Female Breast Carcinoma)** 有效，
目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向，證據主要集中在 BRCA1/2 突變及 HR+/HER2- 亞群。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 軟組織肉瘤、卵巢癌（依文獻描述之歐盟核准適應症；香港無許可證資料） |
| 預測新適應症 | 乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）官方資料（DrugBank 查詢未取得），但根據文獻證據，Trabectedin 是一種 **DNA minor groove 結合劑**，透過干擾轉錄偶合核苷酸切除修復 (TC-NER) 路徑及誘導 DNA-蛋白質交聯產生細胞毒性。這個機轉使其對 **homologous recombination deficiency (HRD)** 腫瘤具有選擇性殺傷力——包括 BRCA1/2 突變型乳癌與三陰性乳癌，與 PARP inhibitor（如 olaparib）併用時具有合成致死（synthetic lethality）協同效應。

Trabectedin 原本已在歐盟核准用於軟組織肉瘤及卵巢癌，兩者與乳癌同屬對 HRD 路徑敏感的腫瘤類型。文獻亦指出其具有調節腫瘤微環境的免疫調節作用（抑制腫瘤相關巨噬細胞），並與 IL-12 併用在三陰性乳癌（TNBC）臨床前模型中展現協同抗腫瘤效果，進一步支持機轉延伸至乳癌的合理性。

需注意的是，現有證據多集中於 **BRCA1/2 突變型** 或 **HR+/HER2-** 特定乳癌亞群，並非泛乳癌適應症的直接機轉延伸，臨床應用範圍可能需限定於這些生物標記陽性族群。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | 已完成 | 76 | 安慰劑對照，評估 trabectedin 對晚期實體腫瘤（含乳癌族群）病人 QT/QTc 間期之影響，樣本數相對充足，設計嚴謹度高 |
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | 已完成 | 9 | Olaparib 於 trabectedin-PLD 反應後之復發卵巢癌維持治療研究，屬 BRCA/HRD 機轉延伸驗證，樣本量小（n=9） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2/RCT | Clinical Breast Cancer | 依 XPG 基因表現評估 trabectedin 於 HR+/HER2- 晚期乳癌之療效 |
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | Phase 2 (單臂) | Clinical Breast Cancer | 蒽環類與 taxane 治療失敗後之晚期乳癌，比較兩種 trabectedin 給藥方案之療效與安全性 |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Annals of Oncology | 首個針對 germline BRCA1/2 突變轉移性乳癌的國際多中心 trabectedin 療效與安全性試驗 |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | 系統性回顧 trabectedin 於乳癌治療的機轉（抑制轉錄調控、降低腫瘤相關巨噬細胞）與應用前景 |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review | Cancer Treatment Reviews | 回顧 trabectedin 作為 BRCA 缺失病人化療選項之機轉與臨床證據 |
| [38366738](https://pubmed.ncbi.nlm.nih.gov/38366738/) | 2024 | Case report | J Dermatol | 個案報告：trabectedin 對多線化療失敗之乳房放射誘發血管肉瘤有效 |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunol Res | Trabectedin 透過清除骨髓抑制性細胞增強 IL-12 於三陰性乳癌之抗腫瘤效果 |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | Preclinical (in vitro) | Toxicology Letters | Trabectedin 於 MCF-7 (HER2-/ER+) 與 MDA-MB-453 (HER2+/ER-) 乳癌細胞株誘導不同程度細胞凋亡 |
| [24941346](https://pubmed.ncbi.nlm.nih.gov/24941346/) | 2014 | Preclinical (in vitro) | European Cytokine Network | Trabectedin 對人類乳癌細胞株及血管內皮細胞具抗血管新生效果 |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 | European J Cancer | Trabectedin 併用 doxorubicin 於晚期軟組織肉瘤與乳癌之藥物動力學與臨床研究（混合族群） |

---

## 香港上市資訊

目前 Trabectedin 在香港**未上市**，無許可證資料。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA minor groove 結合劑，海洋來源生物鹼） |
| 骨髓抑制風險 | 高（文獻報告 Grade 3-4 嗜中性白血球減少約 50%、血小板減少約 20%，來源：PMID 19496709） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | CBC（嗜中性白血球、血小板）、肝功能（ALT/AST，trabectedin 具肝毒性）、腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估資料集缺乏仿單警語、禁忌症及藥物交互作用資料，屬 Blocking 級資料缺口，見下方結論。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖有 2 個已完成臨床試驗與多篇針對 BRCA1/2 突變／HR+/HER2- 乳癌亞群的 Phase 2 研究支持機轉合理性，證據等級達 L2，但目前**缺乏 TFDA/香港仿單警語與禁忌症資料**（Blocking data gap），無法進入安全性初評（S1）。
- Trabectedin 於香港**未上市**，無許可證資料可供對照。

**若要推進需要：**
- 補齊仿單警語／禁忌症資料（DG001，來源：TFDA 官網仿單 PDF）
- 補齊完整作用機轉資料（DG002，來源：DrugBank API）
- 若考慮香港上市，需評估許可證申請路徑
- 針對 BRCA1/2 突變或 HR+/HER2- 乳癌亞群設計更大樣本的確證性試驗（現有 Phase 2 研究樣本數普遍偏小，n=9~76）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

