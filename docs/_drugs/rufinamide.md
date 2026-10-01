---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 777
evidence_level: L5
indication_count: 5
---

# Rufinamide
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

# Rufinamide：從抗癲癇用藥到發熱感染相關癲癇症候群 (FIRES)

## 一句話總結

Rufinamide 是已在香港上市的抗癲癇藥物。
TxGNN 模型預測它可能對**發熱感染相關癲癇症候群 (Febrile Infection-Related Epilepsy Syndrome, FIRES)** 有效。
目前**沒有臨床試驗**，也**沒有文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明具體適應症（屬上市抗癲癇藥物） |
| 預測新適應症 | 發熱感染相關癲癇症候群 (FIRES) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Rufinamide 是一種已上市的抗癲癇藥，其在癲癇發作控制上的角色已為臨床所用，因此知識圖譜中與癲癇相關的鄰近節點可能把它連到 FIRES。

FIRES 是一種難治型、由發炎驅動的癲癇症候群。模型分數很高，但這很可能反映的是圖譜中的「癲癇」共同關聯，而非已驗證的藥理依據。若只靠鈉離子通道這類抗癲癇機轉，未必足以處理 FIRES 的發炎特性，這一點需要專家評估。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-64099 | INOVELON TABLETS 400MG | EISAI (HONG KONG) COMPANY LIMITED |
| HK-64097 | INOVELON TABLETS 100MG | EISAI (HONG KONG) COMPANY LIMITED |
| HK-64098 | INOVELON TABLETS 200MG | EISAI (HONG KONG) COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測（L5），沒有任何臨床試驗或文獻佐證，也缺乏 MOA 與香港仿單的安全性資料，無法進入安全性篩選。
- FIRES 屬發炎驅動型癲癇，單靠抗癲癇機轉的合理性尚未被驗證。

**其他預測適應症（同為 L5，建議皆為 Hold）：**

| 預測適應症 | TxGNN 分數 | 備註 |
|-----------|-----------|------|
| 口周肌陣攣伴失神 (Perioral myoclonia with absences) | 99.51% | 屬全身性癲癇，部分鈉離子通道藥物有加重此類發作的風險，需專家審查機轉與安全性 |
| 光敏感性枕葉癲癇 (Photosensitive occipital lobe epilepsy) | 99.44% | 屬局部性癲癇，概念上與抗癲癇藥相符，但無法由現有資料驗證 |
| 非典型兒童中央顳區棘波癲癇 (Atypical childhood epilepsy with centrotemporal spikes) | 99.44% | 部分鈉離子通道阻斷劑可能使棘慢波活化，推進前需做兒童安全性評估 |
| 隱因性晚發型癲癇性痙攣 (Cryptogenic late-onset epileptic spasms) | 99.44% | 可能與 Rufinamide 用於嚴重兒童癲癇有關，但無試驗或文獻佐證 |

**若要推進需要：**
- 取得香港衛生署核准仿單，補齊警語、禁忌與核准適應症
- 補充 Rufinamide 的作用機轉（MOA）資料（例如查詢 DrugBank）
- 針對 FIRES 檢索臨床試驗與文獻，確認是否有病例報告或觀察性研究
- 邀請癲癇專科專家審查機轉合理性與兒童用藥安全性

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

