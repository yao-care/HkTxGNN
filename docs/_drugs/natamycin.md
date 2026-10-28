---
layout: default
title: Natamycin
parent: 高證據等級 (L1-L2)
nav_order: 610
evidence_level: L1
indication_count: 10
monitor_inn: "NATAMYCIN"
predicted_indications: ["vulvovaginal candidiasis", "candidiasis", "vulvitis", "vulvovaginitis", "trichomonal vulvovaginitis", "postmenopausal atrophic vaginitis", "ulceration of vulva", "vulvar neoplasm", "vaginitis (disease)", "tinea nigra"]
last_modified_at: 2026-10-23
description: "Natamycin：預測新適應症為外陰陰道念珠菌病 (Vulvovaginal Candidiasis)（證據等級 L1）。原適應症：知識圖譜記錄為黴菌性角膜潰瘍"
---

# Natamycin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

## Natamycin：從黴菌性角膜潰瘍到外陰陰道念珠菌病
{: .text-alpha }

## 一句話總結

Natamycin 是多烯類（polyene）抗黴菌藥，知識圖譜中記錄其與黴菌性角膜潰瘍（mycotic corneal ulcer）有關。
TxGNN 模型預測它可能對**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)** 有效，
目前有 **1 個已完成的 Phase 3 臨床試驗**（但為 natamycin 與 lactulose 的複方陰道栓劑）和多篇相關文獻支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄為黴菌性角膜潰瘍（香港許可證未載明核准適應症文字） |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 核准許可證數 | 1 張（有效 1 張） |
| 建議決策 | Proceed with Guardrails |

> 證據等級說明：已完成的 Phase 3 試驗直接研究此疾病，但只有 1 項，且為複方製劑，嚴格而言未完全達到「≥2 個 Phase 3 RCT」的 L1 門檻。另有多項較早期的 natamycin 單方陰道製劑臨床研究（見下方文獻）作為補充，等級宜保守解讀，並在決策中以保留態度看待。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理：natamycin 是多烯大環內酯類抗黴菌藥，會與黴菌細胞膜上的麥角固醇（ergosterol）結合而破壞細胞膜。念珠菌同樣含有麥角固醇，因此在機轉上，對外陰陰道念珠菌病具有合理性。

在臨床上，natamycin 陰道劑型（如 Pimafucin）早已用於陰道念珠菌病。本次資料中的舊文獻顯示，10 天療程的陰道錠劑治癒率約 76%（50 位患者，4 週時維持），另一項研究的治癒率為 88–94%。這些皆為早期、規模小的研究。

需注意：同時預測出的「滴蟲性外陰陰道炎」文獻是 natamycin 與口服 metronidazole 併用，natamycin 的角色是處理合併的酵母菌感染，並非直接對滴蟲有效；而萎縮性陰道炎、外陰潰瘍、外陰腫瘤等預測缺乏任何證據與機轉依據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06411314](https://clinicaltrials.gov/study/NCT06411314) | Phase 3 | 完成 | 218 | 比較 natamycin 100 mg + lactulose 300 mg 陰道栓劑與 Pimafucin（natamycin 100 mg）或單用 lactulose 的優越性，用於非懷孕成年女性的外陰陰道念珠菌病。因為是複方製劑，無法單獨判定 natamycin 的效果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39979898](https://pubmed.ncbi.nlm.nih.gov/39979898/) | 2025 | RCT | BMC Women's Health | natamycin + lactulose 陰道栓劑用於外陰陰道念珠菌病的療效與安全性 |
| [4561566](https://pubmed.ncbi.nlm.nih.gov/4561566/) | 1972 | RCT | Med J Aust | 比較 amphotericin B 與 natamycin 陰道栓劑治療陰道念珠菌病 |
| [6760652](https://pubmed.ncbi.nlm.nih.gov/6760652/) | 1982 | 臨床研究 | Acta Obstet Gynecol Scand | 33 位患者使用 natamycin 陰道錠 10 天，同時治療伴侶者治癒率 94%，安慰劑組 88%，差異不顯著 |
| [6966774](https://pubmed.ncbi.nlm.nih.gov/6966774/) | 1980 | 臨床研究 | N Z Med J | 50 位女性使用 Pimafucin 陰道錠，2 週治癒率 76%，4 週維持 |
| [4584444](https://pubmed.ncbi.nlm.nih.gov/4584444/) | 1973 | 臨床研究 | The Practitioner | natamycin 用於孕期陰道念珠菌病 |
| [12849848](https://pubmed.ncbi.nlm.nih.gov/12849848/) | 2003 | 病例對照 | Reprod Toxicol | 孕期陰道使用 natamycin 的致畸性病例對照研究 |
| [11048415](https://pubmed.ncbi.nlm.nih.gov/11048415/) | 1999 | Review | Ceska Gynekol | 比較 natamycin 與 clotrimazole 治療慢性陰道酵母菌感染 |
| [41412769](https://pubmed.ncbi.nlm.nih.gov/41412769/) | 2025 | 問卷調查 | Ceska Slov Farm | 烏克蘭利維夫外陰陰道念珠菌病處置調查（408 位女性），非療效研究 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41714 | NATACYN OPHTHALMIC SUSPENSION 5% | 眼用懸浮液（依品名） | 資料中未載明 |

此香港許可證為眼用懸浮液，與預測的陰道念珠菌病使用途徑不同；是否有陰道劑型在港上市，資料中未見。

## 安全性考量

- **孕期使用**：有一項病例對照研究（PMID 12849848）探討孕期陰道使用 natamycin 的致畸性，結論細節請查閱原文。
- **用藥限制**：證據僅適用於念珠菌（真菌）病因，不適用於細菌性陰道炎或滴蟲性陰道炎。

其餘安全性資訊（警語、禁忌症、藥物交互作用）請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉合理（麥角固醇結合），且有 1 項已完成的 Phase 3 RCT 與多項歷史臨床研究直接針對陰道念珠菌病，但 Phase 3 為複方製劑，單方 natamycin 的證據多為老舊小型研究。
- 香港現有許可證為眼用劑型，路徑與預測適應症不同。

**若要推進需要：**
- 取得 NCT06411314 / PMID 39979898 的完整結果，分析 natamycin 單獨組（Pimafucin 對照組）的表現
- 確認香港是否有陰道劑型，或需另行申請劑型/適應症
- 取得香港仿單的警語、禁忌症與詳細作用機轉資料
- 將使用範圍限定於確診念珠菌病因，排除細菌性及滴蟲性陰道炎
- 其他預測（外陰炎、外陰陰道炎、泛念珠菌病）僅作為念珠菌感染的延伸，不建議獨立推進；萎縮性陰道炎、外陰潰瘍、外陰腫瘤、滴蟲性外陰陰道炎、黑癬等維持 Hold 或僅作研究問題
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

