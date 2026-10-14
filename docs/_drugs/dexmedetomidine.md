---
layout: default
title: Dexmedetomidine
parent: 僅模型預測 (L5)
nav_order: 268
evidence_level: L5
indication_count: 5
---

# Dexmedetomidine
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

# Dexmedetomidine：從鎮靜用藥到頭痛疾患（Headache Disorder）

## 一句話總結

Dexmedetomidine 是 α2 腎上腺素受體促效劑，在香港以注射濃縮液上市，用於鎮靜。
TxGNN 模型的預測中，證據最完整的是**頭痛疾患 (Headache Disorder)**，目前有 **4 個臨床試驗**和 **7 篇文獻**，但證據主要集中在硬脊膜穿刺後頭痛（PDPH）這個次類型。

> 說明：本報告以預測清單中證據最充分的第 4 名（頭痛疾患）為主要評估對象。第 1 名（腎因性抗利尿不適當症候群，預測分數 99.60%）沒有任何臨床試驗或文獻，且機轉上不合理，故不作為主軸。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前香港許可證資料中未載明核准適應症 |
| 預測新適應症 | 頭痛疾患 (Headache Disorder)，證據集中於硬脊膜穿刺後頭痛 |
| TxGNN 預測分數 | 99.30% |
| 證據等級 | L2（僅限 PDPH）；整體頭痛疾患證據有限 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張（皆為有效的單方許可證） |
| 建議決策 | Proceed with Guardrails（建議以 PDPH 為範圍進行研究） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，dexmedetomidine 是高選擇性的中樞 α2 腎上腺素受體促效劑。臨床試驗摘要指出，它具有鎮痛與抗焦慮作用，並可能因腦血管收縮而降低腦血流量。

PDPH 的特徵是腦脊髓液外漏後的嚴重姿勢性頭痛，與腦血管擴張有關。α2 促效作用可能降低疼痛訊號傳遞並減少腦血管擴張，這是其可能有效的機轉依據。霧化（nebulized）給藥是這些研究採用的新途徑。

需注意：這些證據只針對 PDPH（繼發性頭痛），不能推論到原發性頭痛疾患。多數研究樣本小，設計也不一致。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04910477](https://clinicaltrials.gov/study/NCT04910477) | Phase 3 | 完成 | 90 | 剖腹產後 PDPH：霧化 dexmedetomidine 對比 neostigmine/atropine 與生理食鹽水 |
| [NCT04327726](https://clinicaltrials.gov/study/NCT04327726) | 不適用 (NA) | 完成 | 43 | 脊髓麻醉剖腹產產婦 PDPH：霧化 dexmedetomidine 的療效（隨機對照） |
| [NCT06470854](https://clinicaltrials.gov/study/NCT06470854) | 不適用 (NA) | 完成 | 50 | PDPH：霧化 dexmedetomidine 對比雙側枕大神經阻斷（病例對照） |
| [NCT03513757](https://clinicaltrials.gov/study/NCT03513757) | Phase 4 | 完成 | 40 | 兒童 MRI 鎮靜：propofol 輸注對比 dexmedetomidine 加 propofol；頭痛非主要目標，相關性低 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41120897](https://pubmed.ncbi.nlm.nih.gov/41120897/) | 2025 | 系統性回顧/統合分析 | BMC Anesthesiology | 評估霧化 dexmedetomidine 治療剖腹產後 PDPH 的療效與安全性 |
| [36651373](https://pubmed.ncbi.nlm.nih.gov/36651373/) | 2023 | RCT | Minerva Anestesiologica | 比較霧化 dexmedetomidine 與 neostigmine/atropine 治療 PDPH |
| [33993346](https://pubmed.ncbi.nlm.nih.gov/33993346/) | 2021 | RCT | Journal of Anesthesia | 在 PDPH 保守治療中加入 dexmedetomidine，並以經顱都卜勒評估腦血流動力學效應 |
| [39799300](https://pubmed.ncbi.nlm.nih.gov/39799300/) | 2025 | 病例報告 | BMC Anesthesiology | 兩例產科 PDPH 使用霧化 dexmedetomidine 治療 |
| [31345663](https://pubmed.ncbi.nlm.nih.gov/31345663/) | 2019 | 評論 | Int J Obstet Anesth | 討論霧化 dexmedetomidine 是否為 PDPH 的解方 |

另有 2 篇文獻（PMID 23757186 的 ADHD 藥物過量回顧、PMID 41700262 的後部可逆性腦病變症候群病例）與本適應症相關性低，未列入。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49806 | PRECEDEX INJ 100MCG/ML（輝瑞） | 注射劑 | 資料未載明 |
| HK-66810 | DEXMEDETOMIDINE SANDOZ 濃縮輸注液 200MCG/2ML | 輸注濃縮液 | 資料未載明 |
| HK-67869 | DEXMEDETOMIDINE FRESENIUS 濃縮輸注液 0.2MG/2ML | 輸注濃縮液 | 資料未載明 |
| HK-68011 | DEXMEDETOMIDINE B. BRAUN 濃縮輸注液 200MCG/2ML | 輸注濃縮液 | 資料未載明 |
| HK-66522 | DEXMEDETOMIDINE ORION 濃縮輸注液 200MCG/2ML | 輸注濃縮液 | 資料未載明 |

此為 10 張許可證中的 5 張，其餘許可證同為 dexmedetomidine 單方注射製劑。

## 安全性考量

- **知識圖譜標示的相關疾病（非仿單內容）**：高血壓、低血壓、腎臟疾病、肝臟疾病、膽囊疾病、糖尿病、糖尿病酮酸中毒、房室傳導阻滯、輸尿管積膿。使用前須謹慎評估。
- **藥物交互作用**：共查到 59 筆。中度交互作用包括 morphine、opium、dronabinol、nabilone、diphenoxylate、ethanol、papaverine、sibutramine、amyl nitrite、diazoxide、phentolamine，主要需留意中樞抑制與血壓變化的疊加。
- **血行動力學風險**：dexmedetomidine 可能造成心搏過緩與低血壓，這在頭痛病患，尤其是腦幹型偏頭痛先兆患者中值得留意。

正式的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**（限於 PDPH 範圍；其他預測適應症為 Hold）

**理由：**
- 頭痛疾患中的 PDPH 有 1 個已完成的 Phase 3 試驗、數項 RCT 與 1 篇 2025 年統合分析，臨床訊號一致。但樣本小、不同研究設計混雜，且僅限繼發性頭痛，不宜外推到整體頭痛疾患。
- 其他預測中，偏頭痛 (migraine disorder) 僅有 1 個招募中的試驗（NCT07769255，n=146，尚無結果），屬 L4 研究問題；腎因性 SIAD、腦幹先兆偏頭痛與三叉自主神經性頭痛皆無證據（L5），其中 SIAD 的機轉上不合理（AVPR2 功能獲得性突變作用於受體，α2 促效無法改善），很可能是計算上的假象。

**若要推進需要：**
- 取得完整仿單，確認核准適應症、警語與禁忌症
- 取得詳細作用機轉資料
- 進行較大規模、設計嚴謹的多中心 RCT，確認霧化 dexmedetomidine 對 PDPH 的療效與劑量
- 確認霧化給藥途徑在香港的法規適用性與製劑可得性
- 建立心率、血壓的監測計畫，特別針對低血壓與房室傳導阻滯高風險族群
- 持續追蹤 NCT07769255 的偏頭痛試驗結果
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

