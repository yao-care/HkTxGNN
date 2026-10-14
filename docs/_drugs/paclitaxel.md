---
layout: default
title: Paclitaxel
parent: 高證據等級 (L1-L2)
nav_order: 656
evidence_level: L2
indication_count: 5
---

# Paclitaxel
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

# Paclitaxel：從卵巢癌到女性乳癌

## 一句話總結

Paclitaxel（太平洋紫杉醇）是一種紫杉烷類抗微管藥物，知識圖譜中的原適應症以卵巢癌及相關卵巢腫瘤為主。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過乳癌其實已是 paclitaxel 的既定標準用藥，嚴格來說屬於已確立的用途，而非全新的再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 卵巢癌（香港許可證未列出核准適應症文字，此處依知識圖譜適應症） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.995% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載。根據已知藥理資訊，paclitaxel 會穩定微管、阻止有絲分裂紡錘體解聚，使快速分裂的癌細胞停滯於 G2/M 期並走向凋亡。

卵巢癌與乳癌同屬婦科及荷爾蒙相關的實體腫瘤，且 paclitaxel 的細胞毒性並不依賴荷爾蒙受體訊號，因此機轉上適用於乳癌。文獻也指出，paclitaxel 與 docetaxel 已被廣泛接受為晚期乳癌、肺癌與卵巢癌的循證治療成分。

因此，本預測更接近「確認既有標準用途」。另外，TxGNN 同時預測了雌激素受體陰性乳癌、荷爾蒙抗性乳癌與雌激素受體陽性乳癌，其中雌激素受體陽性乳癌的證據等級為 L1，但該評級反映的是有涉及 paclitaxel 的 Phase 3 試驗，並非 paclitaxel 單獨的頭對頭證據。「Ehrlich 腫瘤癌」僅有小鼠模型研究（L5），不屬於臨床適應症，建議 Hold。

---

## 臨床試驗證據

以下列出與 paclitaxel 最相關的 10 個試驗（共 40 個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00003539](https://clinicaltrials.gov/study/NCT00003539) | Phase 2 | 完成 | 50 | 每週 paclitaxel 加 trastuzumab 用於轉移性乳癌 |
| [NCT00006120](https://clinicaltrials.gov/study/NCT00006120) | Phase 2 | 未知 | 未提供 | 隨機比較 docetaxel 或 paclitaxel 兩種給藥時程於轉移性乳癌 |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | 完成 | 652 | 紫杉烷化療加 lapatinib 或 trastuzumab 用於 HER2 陽性轉移性乳癌 |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | 完成 | 455 | Neo-ALTTO：新輔助 lapatinib／trastuzumab 加 paclitaxel 用於 HER2 陽性乳癌 |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | 完成 | 未提供 | Gemcitabine 加 paclitaxel 對比單用 paclitaxel 於晚期乳癌 |
| [NCT00513292](https://clinicaltrials.gov/study/NCT00513292) | Phase 3 | 完成 | 280 | FEC 後接 paclitaxel＋trastuzumab 對比相反順序，用於 HER2 陽性可手術乳癌 |
| [NCT00075270](https://clinicaltrials.gov/study/NCT00075270) | Phase 3 | 完成 | 580 | Lapatinib 加 paclitaxel 對比單用 paclitaxel 於第一線晚期乳癌 |
| [NCT01822314](https://clinicaltrials.gov/study/NCT01822314) | Phase 3 | 完成 | 632 | ETNA：新輔助 nab-paclitaxel 對比溶劑型 paclitaxel（HER2 陰性高風險乳癌） |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | 完成 | 478 | 劑量密集 FE75C 後接 docetaxel 對比 paclitaxel 作輔助化療 |
| [NCT00002826](https://clinicaltrials.gov/study/NCT00002826) | Phase 2 | 完成 | 36 | PSC 833 調節 paclitaxel 多重抗藥性於轉移性乳癌 |

**說明：**
- 已完成的 Phase 3 試驗多為 paclitaxel 作為組合或比較用藥，paclitaxel 不一定是唯一的研究變項。
- 多個試驗屬 Phase 1/2 組合試驗，或 paclitaxel 僅為組合夥伴，未列於上表。
- 另有數個試驗已撤回（如 NCT03058939），不納入主要證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22331946](https://pubmed.ncbi.nlm.nih.gov/22331946/) | 2012 | Phase 3 試驗 | J Clin Oncol | 比較每週 paclitaxel 與 docetaxel 合併 capecitabine 於可手術乳癌的無復發存活 |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 臨床試驗 | Cancer | Doxorubicin 加 paclitaxel 治療晚期乳癌，並探討先前輔助 anthracycline 治療的影響 |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | 研究／回顧 | Cancer | Paclitaxel 用於發炎性乳癌的多模式治療 |
| [9296218](https://pubmed.ncbi.nlm.nih.gov/9296218/) | 1997 | 劑量探索研究 | Ann Oncol | Paclitaxel 加 cyclophosphamide 於晚期乳癌的最大耐受劑量 |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | 紫杉烷為晚期乳癌、肺癌與卵巢癌的循證治療成分；paclitaxel 在美國獲准用於淋巴結陽性早期乳癌輔助治療 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Paclitaxel 與 docetaxel 於乳癌及卵巢癌的適應症擴展 |
| [10898354](https://pubmed.ncbi.nlm.nih.gov/10898354/) | 2000 | Review | Cancer | 乳癌化療發展概述 |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | 機轉研究 | Nat Commun | TEKT4 變異與乳癌對 paclitaxel 的抗藥性 |
| [20665703](https://pubmed.ncbi.nlm.nih.gov/20665703/) | 2011 | 前臨床 | J Cell Physiol | ZD6474 增強 paclitaxel 對乳癌細胞的抗增殖與促凋亡作用 |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | 計算／前臨床 | Chem Biol Drug Des | Paclitaxel 組合治療乳癌的潛力與體內生物標記 |

---

## 香港上市資訊

目前香港共有 17 張有效許可證（皆為單一成分，無已註銷者）。資料中未載明劑型與核准適應症文字，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37867 | TAXOL INJ 6MG/ML（DKSH） | 注射劑 | 資料未載明 |
| HK-40639 | ANZATAX INJ 150MG/25ML VIAL（Pfizer） | 注射劑 | 資料未載明 |
| HK-62459 | ABRAXANE POWDER FOR INJECTABLE SUSPENSION 100MG（BMS） | 注射用懸浮液粉末 | 資料未載明 |
| HK-68817 | PAZENIR POWDER FOR DISPERSION FOR INFUSION 100MG（Teva） | 輸注用分散液粉末 | 資料未載明 |
| HK-60886 | PACLITAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/16.7ML（Fresenius Kabi） | 輸注濃縮液 | 資料未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（紫杉烷類，微管穩定劑） |
| 骨髓抑制風險 | 高（知識圖譜顯示與嗜中性白血球低下、血小板低下、無顆粒性白血球症等禁忌關聯） |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝功能（含膽紅素）、腎功能、周邊神經病變評估、過敏反應監測 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

具體警語與劑量調整請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（非仿單文字）：嗜中性白血球低下、血小板低下、無顆粒性白血球症、貧血、肝病、膽囊疾病、高膽紅素血症（含 Gilbert 症候群）、腎臟疾病、周邊神經病變、心肌梗塞、猝死性心臟驟停、氣喘、糖尿病（含酮酸中毒）、低血壓、乾癬等。
- **藥物交互作用**：資料共 100 筆，以下為主要代表：
  - 中度：Aprepitant、Cimetidine、Clarithromycin、Clotrimazole、Dexamethasone、Eliglustat、Metronidazole、Miconazole、Rolapitant、Rosuvastatin、Simvastatin、Tinidazole、Troglitazone
  - 輕度：Ascorbic acid、Levofloxacin
  - 等級未知：Glimepiride、Doxycycline、Morphine、Metformin、Omeprazole

其餘仿單警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 乳癌用藥已有多個已完成的 Phase 3 試驗涉及 paclitaxel，且機轉合理；但本次所列試驗多以組合療法為主，paclitaxel 單獨作為研究變項的證據有限，因此評為 L2。這屬於既定標準用途，並非嚴格意義上的新適應症。
- 該藥已在香港上市多年，但血液毒性與神經毒性風險高，需要嚴格防護。

**若要推進需要：**
- 取得香港衛生署核准適應症文字與仿單，確認乳癌是否已列入核准適應症
- 取得 DrugBank 作用機轉資料
- 針對各乳癌亞型（HER2 陽性、三陰性、荷爾蒙受體陽性／抗性）釐清 paclitaxel 的角色與優先順序
- 建立血液學與神經毒性監測計畫，並評估溶劑型與白蛋白結合型（nab-paclitaxel）劑型的選擇
- 「Ehrlich 腫瘤癌」僅為小鼠模型訊號，建議 Hold，不予推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

