---
layout: default
title: Benzoin
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Benzoin：預測新適應症為外陰陰道念珠菌病 (Vulvovaginal Candidiasis)（證據等級 L5）。原適應症：肛門生殖器 HPV 感染、尋常疣、角化性疾病、喉部乳突瘤"
monitor_inn: "Benzoin"
predicted_indications: ["vulvovaginal candidiasis", "variola minor infection", "viral eye infection", "Klebsiella infectious disease", "vibrio infectious disease", "ear infection", "noma", "chorioamnionitis", "infective arthritis"]
---

# Benzoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Benzoin：從肛門生殖器人類乳突病毒感染到外陰陰道念珠菌病
{: .text-alpha }

## 一句話總結

Benzoin（安息香）是傳統樹脂類外用製劑，原本用於肛門生殖器 HPV 感染、尋常疣、角化性疾病與喉部乳突瘤。
TxGNN 模型預測排名第一的新適應症為**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)**，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。
相對地，**人類乳突病毒感染 (HPV infection)** 有 12 篇文獻，但多與原適應症重疊（見下文）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肛門生殖器 HPV 感染、尋常疣、角化性疾病、喉部乳突瘤（香港許可證未載明適應症文字） |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 97.79% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Benzoin 是樹脂類外用製劑（安息香酊），具有輕度的抗菌、抗septic與保護特性，機轉上可能與抗黴菌活性有關，但這僅是推測，並無直接證據。

TxGNN 對此適應症給出高分（97.79%），但這是純計算預測，沒有臨床或文獻佐證。

值得注意的是，在其他預測適應症中，證據最多的是 **HPV 感染**（L3）。文獻顯示 Benzoin 複方酊劑主要作為 podophyllin 的載體與保護性固定劑，抗病毒效果來自 podophyllin 而非 Benzoin 本身。因此這較接近原有用途的重疊，而非真正的藥物再利用。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對排名第一的外陰陰道念珠菌病：目前無相關文獻。

以下為證據最多的預測適應症「人類乳突病毒感染」（排名第 3，TxGNN 分數 96.59%）之主要文獻，供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9557098](https://pubmed.ncbi.nlm.nih.gov/9557098/) | 1998 | RCT | Singapore Med J | 比較 0.5%/0.25% podophyllin 乙醇液與 25% podophyllin 安息香酊治療陰莖疣的療效與皮膚刺激 |
| [7016248](https://pubmed.ncbi.nlm.nih.gov/7016248/) | 1981 | RCT | Br J Vener Dis | 雙盲比較 10% 與 25% podophyllin（安息香複方酊）治療肛門生殖器疣；治療後僅 22% 無疣，兩組無顯著差異 |
| [3592587](https://pubmed.ncbi.nlm.nih.gov/3592587/) | 1987 | Cohort | Ann Acad Med Singap | 比較醫院施用與自行施用 25% podophyllin 安息香複方酊；六週反應率分別為 66% 與 72% |
| [8399504](https://pubmed.ncbi.nlm.nih.gov/8399504/) | 1993 | Audit | Int J STD AIDS | 生殖器疣治療稽核，顯示處置策略不明確、監測不佳 |
| [11126083](https://pubmed.ncbi.nlm.nih.gov/11126083/) | 2000 | Cohort | West Afr J Med | 伊巴丹性病門診生殖器 HPV 感染盛行率調查 |
| [1674482](https://pubmed.ncbi.nlm.nih.gov/1674482/) | 1991 | Cohort | Int J Gynaecol Obstet | 尼日利亞外陰疣型態回溯分析，與念珠菌病、滴蟲病有明顯關聯 |
| [4043973](https://pubmed.ncbi.nlm.nih.gov/4043973/) | 1985 | Case report | Genitourin Med | 兒童尖圭濕疣 4 例，局部使用 25% podophyllin 安息香複方酊反應良好 |
| [458391](https://pubmed.ncbi.nlm.nih.gov/458391/) | 1979 | Case report/Review | J Fam Pract | podophyllum 樹脂安息香複方酊外用於外陰濕疣後發生嚴重毒性（骨髓、肝臟、中樞神經） |
| [4801097](https://pubmed.ncbi.nlm.nih.gov/4801097/) | 1973 | Case series | Arch Gynakol | podophyllin-安息香療法後尖圭濕疣的光學與電子顯微鏡觀察 |
| [4801497](https://pubmed.ncbi.nlm.nih.gov/4801497/) | 1973 | Case series | Arch Gynakol | 局部 podophyllin-安息香治療後的超微結構變化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43203 | COMPOUND BENZOIN TINCTURE | 未載明 | 未載明 |
| HK-42429 | EXTRACT FOR MAKING CO BENZOIN TINCTURE | 未載明 | 未載明 |

兩張許可證均為單一成分、狀態有效，持證商為 TRANSO-PHARM (HONG KONG) LIMITED。

---

## 安全性考量

- **藥物交互作用**：資料庫查無相關紀錄。
- **其他風險提示（來自文獻）**：Benzoin 複方酊常與 podophyllin 合用，有案例報告顯示大面積外用 podophyllum 會造成嚴重全身毒性，包括骨髓、肝臟與中樞神經；此毒性主要與 podophyllin 相關。若考慮眼部或耳部使用，也有刺激性與耳毒性疑慮；孕期安全性尚未確立。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（外陰陰道念珠菌病）沒有任何臨床試驗或文獻，僅為模型預測（L5）。
- 證據最多的 HPV 感染，其文獻主要反映 Benzoin 作為 podophyllin 載體的既有用途，並非 Benzoin 本身的新療效，且伴隨 podophyllum 毒性疑慮。其他預測適應症（如天花、Klebsiella、Vibrio、諾馬病、絨毛膜羊膜炎、感染性關節炎）缺乏證據，且外用樹脂在生物學上難以治療深部或全身性感染。

**若要推進需要：**
- 取得 Benzoin 的作用機轉資料（MOA），並釐清其本身是否具抗黴菌活性
- 進行體外抗念珠菌活性試驗，作為最低限度的前臨床證據
- 取得香港衛生署仿單，補齊適應症、警語與禁忌症
- 評估陰道黏膜使用的刺激性與安全性（含孕期）
- 釐清 Benzoin 單獨使用與 podophyllin 合併使用之效果與毒性歸屬
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

