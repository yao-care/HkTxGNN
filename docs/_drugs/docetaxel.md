---
layout: default
title: Docetaxel
parent: 高證據等級 (L1-L2)
nav_order: 211
evidence_level: L1
indication_count: 10
---

# Docetaxel
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Docetaxel：從廣效固態腫瘤化療到女性乳癌

## 一句話總結

Docetaxel 是 taxane 類第二代微管穩定劑，全球多個國家已核准用於乳癌、肺癌、前列腺癌等固態腫瘤，但香港目前尚無上市許可。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，預測分數高達 **99.90%**，
目前有 **50 個臨床試驗**和 **20 篇文獻**支持此方向，其中包含多個超大型 Phase 3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 廣效固態腫瘤（香港未登記） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Docetaxel 為 paclitaxel 的半合成衍生物，屬第二代 taxane。其核心作用機轉為：以高親和力（約為 paclitaxel 的 2 倍）與 **β-tubulin 結合，促進微管聚合並抑制解聚**，使癌細胞週期停滯於 G2/M 期，進而誘發凋亡（apoptosis）。相較於一代 taxane，docetaxel 在細胞內滯留時間更長，抗腫瘤效力更為持久。

乳癌細胞高度增殖且有絲分裂活躍，微管系統是其分裂的關鍵依賴結構，因此對 taxane 類藥物天然敏感。Docetaxel 的療效已在三種主要乳癌亞型中獲得充分驗證：在**三陰性乳癌（TNBC）**中，作為新輔助化療骨幹藥物；在 **HER-2 陽性乳癌**中，與 trastuzumab 協同，同時發揮 ADCC 效應與直接細胞毒性；在**荷爾蒙受體陽性（HR+）**高風險患者中，則用於輔助化療。

TxGNN 的預測與上述作用機轉高度吻合，更有多個超大規模 Phase 3 RCT（包含 n=2,411 及 n=3,010 的里程碑試驗）的強力支撐，使本預測臨床可信度達到最高等級（L1）。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | 完成 | 2,411 | 比較術前 AC、術前 AC→docetaxel、及術前 AC 序貫術後 docetaxel 於 Stage II/III 乳癌，奠定 taxane 在乳癌中的一線地位 |
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | 完成 | 3,010 | Docetaxel 75mg/m² + epirubicin 75mg/m² vs FEC100 於淋巴結陽性乳癌；HER2+++ 族群序貫評估 herceptin 效益 |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | 完成 | 1,384 | EC→docetaxel vs ET→capecitabine 輔助化療方案比較，HER2 陰性淋巴結陽性乳癌 |
| [NCT00615602](https://clinicaltrials.gov/study/NCT00615602) | Phase 3 | 完成 | 489 | Trastuzumab 6 vs 12 個月合併 dose-dense docetaxel（序貫 FE75C 後）於 HER2+ 淋巴結陽性乳癌 |
| [NCT02980965](https://clinicaltrials.gov/study/NCT02980965) | Phase 3 | 完成 | 249 | 新輔助化療合併 vs 不合併內分泌療法比較，ER+/HER2- 乳癌（含 docetaxel 骨幹方案） |
| [NCT00015938](https://clinicaltrials.gov/study/NCT00015938) | Phase 2 | 完成 | 95 | Docetaxel + vinorelbine + filgrastim 於 HER-2 陰性 Stage IV 乳癌（Grade A 直接相關） |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | 完成 | 45 | 新輔助 bevacizumab + docetaxel + carboplatin 於三陰性乳癌（NEAT 試驗，Grade A 直接相關） |
| [NCT00712881](https://clinicaltrials.gov/study/NCT00712881) | Phase 2 | 完成 | 126 | MYOCET + cyclophosphamide + trastuzumab 序貫 docetaxel + trastuzumab 新輔助治療 HER2+ Stage II/III 乳癌 |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase 2 | 未知 | 99 | Docetaxel + gemcitabine 新輔助化療多中心研究，評估局部進展期乳癌療效與安全性 |
| [NCT02897050](https://clinicaltrials.gov/study/NCT02897050) | Phase 2 | 暫停 | 170 | Docetaxel ± 節拍式 cyclophosphamide/capecitabine 序貫 FEC 於三陰性乳癌（目前暫停中） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT (Phase 3) | J Clin Oncol | ABC 試驗群：TC6 vs 多種 TaxAC 方案，比較 taxane 加入蒽環素方案的附加效益（n 達數千） |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Phase 2 | Breast Cancer | Docetaxel + cyclophosphamide + trastuzumab（HER-TC）新輔助化療 HER2+ 乳癌 pCR 率分析 |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Cohort | Br J Cancer | 基因表現圖譜預測 trastuzumab-docetaxel 治療之病理完全緩解（pCR）預測因子 |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | RCT (Phase 2b) | J Clin Oncol | Dose-dense doxorubicin + docetaxel ± tamoxifen 於可手術乳癌新輔助治療的病理緩解率評估 |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine + docetaxel + epirubicin（TEX 方案）於未治療局部進展/轉移性乳癌活性及安全性 |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Docetaxel 輔助化療與乳癌相關淋巴水腫發生率關聯性研究（Stage II/III） |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 | Tumori | 週制 docetaxel + gemcitabine 劑量尋優研究，用於蒽環素治療後轉移性乳癌 |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 2 | Oncology | Docetaxel + vinorelbine 組合用於轉移性乳癌及 NSCLC 的早期療效與毒性資料 |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase 2 | Breast Cancer | CEF → docetaxel 新輔助化療日本多中心中期分析（JBCRG），n=79，臨床緩解率及安全性 |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Docetaxel 臨床前生物活性及早期臨床試驗的奠基性系統綜述 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Taxane 類，微管穩定劑） |
| 骨髓抑制風險 | 高（嗜中性白血球減少為劑量限制性毒性，Grade 3-4 發生率高，建議評估預防性 G-CSF） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含白血球分類計數）、肝功能（ALT/AST/膽紅素/鹼性磷酸酶）、腎功能、周邊神經毒性（依 CTCAE 分級評估）、體液滯留（體重、水腫程度） |
| 處置防護 | 需依細胞毒性藥物處置規範（生物安全防護）操作；給藥前須預投類固醇（如 dexamethasone 8mg bid × 3 天）以預防超敏反應及體液滯留綜合症 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Docetaxel 用於女性乳癌擁有多個大型 Phase 3 RCT（包含 n=2,411、n=3,010、n=1,384 等里程碑研究）的最高等級證據，TxGNN 預測分數達 99.90%，證據等級為 L1；惟香港目前尚無正式上市許可（0 張許可證），需先完成法規引進評估並取得完整安全性資訊方可推進。

**若要推進需要：**
- 向香港衛生署申請藥物引進許可或個案授權（Special Purpose Approval）
- 補充完整安全性資訊：取得原廠仿單（含 FDA/EMA 警語、禁忌症、藥物交互作用清單）
- 依乳癌亞型（TNBC / HER2+ / HR+ 高風險）制定精準適應症策略，避免適用範圍過寬
- 建立骨髓抑制管理計畫，評估 G-CSF（filgrastim / pegfilgrastim）預防性使用方案
- 制定周邊神經毒性、體液滯留及超敏反應的監測流程與分級處置規範
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

