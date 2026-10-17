---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 428
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Griseofulvin：預測新適應症為蠅蛆症 (Myiasis)（證據等級 L5）。原適應症：足癬、體癬、甲癬、癬類感染、鼠蹊與肛周皮癬菌病、鬚癬、頭皮或鬚部皮癬菌病"
monitor_inn: "GRISEOFULVIN"
predicted_indications: ["myiasis", "furuncular myiasis", "wound myiasis", "creeping myiasis", "echinococcus granulosus infectious disease"]
---

# Griseofulvin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Griseofulvin：從皮癬菌感染（癬類）到蠅蛆症

## 一句話總結

Griseofulvin 是一種抗黴菌藥物，原本用於治療足癬、體癬、甲癬、頭皮與鬚部皮癬菌感染等皮膚癬菌病。
TxGNN 模型預測它可能對**蠅蛆症 (Myiasis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 足癬、體癬、甲癬、癬類感染、鼠蹊與肛周皮癬菌病、鬚癬、頭皮或鬚部皮癬菌病 |
| 預測新適應症 | 蠅蛆症 (Myiasis) |
| TxGNN 預測分數 | 99.41% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

註：香港許可證資料中未提供核准適應症文字，上列原適應症取自 TxGNN 知識圖譜的適應症資料。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般已知 Griseofulvin 是抗黴菌藥物，會結合微管蛋白 (tubulin)，干擾黴菌的微管功能與有絲分裂。

蠅蛆症是雙翅目蒼蠅幼蟲造成的寄生蟲感染，與皮膚癬菌病的病原體完全不同。目前**沒有已知的機轉依據**，可說明靠微管蛋白為標的的作用能在臨床可達劑量下影響幼蟲發育。0.994 的高分僅是計算模型的預測，可能反映的是知識圖譜中與其他抗寄生蟲藥物的網路相近性。

另外，蠅蛆症的標準治療（移除幼蟲、ivermectin）本來就有效，未滿足的醫療需求低。

同樣被預測的還有其他蠅蛆症亞型：癤性蠅蛆症 (furuncular myiasis)、傷口蠅蛆症 (wound myiasis)、遊走性蠅蛆症 (creeping myiasis)，三者分數皆為 99.34%，且完全相同。這顯示預測很可能是從上層疾病節點傳遞而來，並非各自獨立的證據。

排名第 5 的**細粒棘球絨蟲感染 (Echinococcus granulosus，分數 99.32%)** 有一點概念上的類比：治療該病的 benzimidazole 類藥物（albendazole、mebendazole）同樣作用於微管蛋白。但 Griseofulvin 並無證據顯示能結合該寄生蟲的 β-tubulin，同樣沒有前臨床資料，因此仍屬推測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34137 | GRISEOFULVIN TAB 125MG (VICKMANS) | 錠劑（125 mg） | 未提供 |
| HK-33380 | GRISEOFULVIN TAB 500MG（APT PHARMA） | 錠劑（500 mg） | 未提供 |
| HK-26326 | FUYOU TAB 500MG | 錠劑（500 mg） | 未提供 |
| HK-66191 | NACOSIL GRISEOFULVIN TABLETS 250MG | 錠劑（250 mg） | 未提供 |
| HK-31024 | MEDOFULVIN 125 TAB 125MG | 錠劑（125 mg） | 未提供 |

香港共有 9 張有效單方許可證，皆為上市中，無已註銷者。此處僅列出 5 張主要許可證。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜的藥物－疾病禁忌關聯，並非仿單內容）：
  - 肝衰竭
  - 紫質症（含遺傳性紫質症、紫質代謝疾病）
  - 系統性紅斑狼瘡（含兒童型）
  - 物質濫用／依賴
  - 顆粒球缺乏症與各類嗜中性白血球低下症（含先天性、週期性、體質性嗜中性白血球低下等）
- **藥物交互作用**：資料庫共查得 100 筆，其中中度交互作用包括：
  - 抗凝血劑與抗血小板藥：Warfarin、Apixaban、Rivaroxaban、Ticagrelor、Dicoumarol
  - 降血糖藥：Saxagliptin、Linagliptin、Repaglinide
  - 止吐藥與其他：Aprepitant、Rolapitant、Naloxegol、Eliglustat、Nitisinone
  - 抗瘧與驅蟲藥：Artemether、Mefloquine、Praziquantel

  輕度者如 Acetylsalicylic acid、Liraglutide。

香港仿單的警語與禁忌資料尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測證據等級僅為 L5，無任何臨床試驗或文獻，且沒有合理的機轉連結。多個蠅蛆症亞型的分數完全相同，顯示預測來自疾病本體的傳遞效應。
- 現有標準治療（移除幼蟲、ivermectin）已有效，新增用途的需求低。

**若要推進需要：**
- 取得 Griseofulvin 的作用機轉資料
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 若仍想探索，應先做體外試驗（如對幼蟲或棘球絨蟲原頭節的活性測試），再考慮後續研究
- 確認給藥途徑的相容性（目前尚待評估）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

