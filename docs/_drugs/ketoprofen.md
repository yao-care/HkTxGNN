---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 5
---

# Ketoprofen
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

# Ketoprofen：從類風濕性關節炎到肢端中肢發育不良（Hunter-Thompson 型）

## 一句話總結

Ketoprofen 是一種非類固醇消炎止痛藥（NSAID），原本用於類風濕性關節炎、骨關節炎與關節病變。
TxGNN 模型預測它可能對**肢端中肢發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type)** 有效。
然而目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測，且機轉上缺乏合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎、骨關節炎、關節病變（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 肢端中肢發育不良，Hunter-Thompson 型 (Acromesomelic dysplasia, Hunter-Thompson type) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ketoprofen 是非選擇性 COX 抑制劑，具消炎與止痛作用，在關節炎類疾病中的療效已被證實。

Hunter-Thompson 型肢端中肢發育不良是罕見的骨骼疾病，由 CDMP1/GDF5 功能喪失突變導致軟骨形成受損。Ketoprofen 並不作用於 GDF5/BMP 訊號路徑，因此**機轉上沒有已知的關聯**。

極高的預測分數（99.98%）較可能反映知識圖譜中，該疾病與原適應症（關節病變、骨關節炎）在骨骼與關節術語上的鄰近性，而非生物學上的理由。頂多只能做關節疼痛的症狀緩解，無法改變疾病本身。

其他排名前列的預測（brachyolmia-amelogenesis imperfecta 症候群、myosclerosis、brachyolmia、colobomatous microphthalmia-rhizomelic dysplasia 症候群）同樣沒有試驗或文獻支持，且機轉上皆缺乏合理連結。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 20 張有效許可證（皆為單一成分），以下列出 5 張主要許可證，其餘多為貼布劑。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-18544 | KETOFEN CAP 50MG（膠囊） | WILCOME PHARMACEUTICAL CO LTD |
| HK-36101 | FASTUM GEL 2.5%W/W（凝膠） | A. MENARINI HONG KONG LIMITED |
| HK-59428 | KETOFEN GEL 2.5%（凝膠） | HOVID LIMITED |
| HK-67384 | MOHRUS PATCH 40MG（貼布） | HISAMITSU PHARMACEUTICAL (HONG KONG) CO., LIMITED |
| HK-67212 | KETOTOP PLASTER 30MG（貼布） | ZUELLIG PHARMA LIMITED |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜，非仿單內容）：高血壓、肝衰竭、腎臟疾病、消化性潰瘍（含活動性）、凝血疾病、心肌梗塞、冠狀動脈血栓、血紅素病變、心血管疾病、心臟病、輸尿管積膿。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Acetylsalicylic acid（阿斯匹靈）、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide（皮質類固醇）、Metformin、Glimepiride、Chlorpropamide（降血糖藥）、Mesalazine、Balsalazide、Naltrexone
  - 輕度：Famotidine、Ranitidine、Cimetidine、Linaclotide

香港仿單的警語與禁忌症資料尚未取得，詳細安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型推論（L5），沒有任何臨床試驗或文獻佐證，且 Ketoprofen 與 GDF5/BMP 訊號路徑無已知關聯。
- 高分疑為知識圖譜鄰近性造成的假象。此外，知識圖譜標示心血管、腎臟、消化道等多項禁忌，對需長期使用的罕見疾病族群風險不容忽視。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並驗證是否有任何生物學上的連結
- 取得香港仿單的警語與禁忌症
- 進行前臨床研究（如 GDF5 突變細胞或動物模型），再考慮臨床試驗
- 若僅考慮症狀緩解（關節疼痛），應視為一般 NSAID 使用，不屬藥物再利用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

